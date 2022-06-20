import json
import requests
import time
import curlify

userName = 'admin'
firstName = 'admin'
lastName = 'admin'
password = 'Administr@tor123'
email = "interlink@admin.com"
headers = {'content-type': 'application/json', 'Authorization': '_dremionull'}
dremioServer = 'http://localhost:9047'


def apiGet(endpoint):
    return json.loads(requests.get('{server}/api/v3/{endpoint}'.format(server=dremioServer, endpoint=endpoint), headers=headers).text)


def apiPost(endpoint, body=None):
    response = requests.post('{server}/api/v3/{endpoint}'.format(server=dremioServer,
                         endpoint=endpoint), headers=headers, data=json.dumps(body))

    print(response.__dict__)
    text = response.text
    assert response.status_code in [200, 409]

    # a post may return no data
    if (text):
        return json.loads(text)
    else:
        return None


def apiPut(endpoint, body=None):
    return requests.put('{server}/api/v3/{endpoint}'.format(server=dremioServer, endpoint=endpoint), headers=headers, data=json.dumps(body)).text


def apiDelete(endpoint):
    return requests.delete('{server}/api/v3/{endpoint}'.format(server=dremioServer, endpoint=endpoint), headers=headers)


def login(username, password):
    # we login using the old api for now
    loginData = {'userName': username, 'password': password}
    response = requests.post(
        '{server}/apiv2/login'.format(server=dremioServer), headers=headers, data=json.dumps(loginData))
    data = json.loads(response.text)

    # retrieve the login token
    token = data['token']
    return {'content-type': 'application/json', 'Authorization': '_dremio{authToken}'.format(authToken=token)}


def querySQL(query):
    queryResponse = apiPost('sql', body={'sql': query})
    jobid = queryResponse['id']
    return jobid


response = requests.put('{server}/apiv2/bootstrap/firstuser'.format(server=dremioServer), headers=headers, data=json.dumps({
    "userName": userName,
    "firstName": firstName,
    "lastName": lastName,
    "createdAt": int(time.time()),
    "email": email,
    "password": password,
}))

headers = login(userName, password)

# https://docs.dremio.com/software/rest-api/sources/sources/

# POSTGRES SOURCES
apiPost('catalog', body={
    "entityType": "source",
    "name": "catalogue",
    "description": "catalogue data",
    "type": "POSTGRES",
    "config": {
        "username": "postgres",
        "password": "changethis",
        "hostname": "db",
        "port": "5432",
        "authenticationType": "MASTER",
        "fetchSize": "0",
        "databaseName": "catalogue_production"
    },
})

apiPost('catalog', body={
    "entityType": "source",
    "name": "coproduction",
    "description": "coproduction data",
    "type": "POSTGRES",
    "config": {
        "username": "postgres",
        "password": "changethis",
        "hostname": "db",
        "port": "5432",
        "authenticationType": "MASTER",
        "fetchSize": "0",
        "databaseName": "coproduction_production"
    },
})

# ELASTICSEARCH SOURCE
apiPost('catalog', body={
    "entityType": "source",
    "name": "elastic",
    "description": "elasticsearch for logs",
    "type": "ELASTIC",
    "config": {
        "username": "elastic",
        "password": "elastic",
        "hostList": [{"hostname": "newelasticsearch", "port": "27017"}],
        "authenticationType": "MASTER",
    },
})
