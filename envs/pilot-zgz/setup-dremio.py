import json
import requests
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config():
    userName = os.environ.get("DREMIO_USERNAME")
    firstName = os.environ.get("DREMIO_USERNAME")
    lastName = os.environ.get("DREMIO_USERNAME")
    ## needs to be with uppercase, lowercase, digits and special character
    password = os.environ.get("DREMIO_PASSWORD")
    email = os.environ.get("DREMIO_EMAIL")
    dremioServer = "http://localhost:9047"
    token = None

    def get_headers(self):
        if self.token:
            return {'content-type': 'application/json',
                    'Authorization': '_dremio{authToken}'.format(authToken=self.token)}
        return {'content-type': 'application/json', 'Authorization': '_dremionull'}


config = Config()


def apiGet(endpoint):
    return json.loads(requests.get('{server}/api/v3/{endpoint}'.format(server=config.dremioServer, endpoint=endpoint),
                                   headers=config.get_headers()).text)


def apiPost(endpoint, body=None):
    response = requests.post('{server}/api/v3/{endpoint}'.format(server=config.dremioServer,
                                                                 endpoint=endpoint), headers=config.get_headers(),
                             data=json.dumps(body))

    # print(response.__dict__)
    text = response.text
    print(response.status_code, text)
    assert response.status_code in [200, 409]

    # a post may return no data
    if (text):
        return json.loads(text)
    else:
        return None


def apiPut(endpoint, body=None):
    return requests.put('{server}/api/v3/{endpoint}'.format(server=config.dremioServer, endpoint=endpoint),
                        headers=config.get_headers(), data=json.dumps(body)).text


def apiDelete(endpoint):
    return requests.delete('{server}/api/v3/{endpoint}'.format(server=config.dremioServer, endpoint=endpoint),
                           headers=config.get_headers())


def login():
    # we login using the old api for now
    loginData = {'userName': config.userName, 'password': config.password}
    response = requests.post(
        '{server}/apiv2/login'.format(server=config.dremioServer), headers=config.get_headers(),
        data=json.dumps(loginData))
    data = json.loads(response.text)

    # retrieve the login token
    config.token = data['token']


def querySQL(query):
    queryResponse = apiPost('sql', body={'sql': query})
    jobid = queryResponse['id']
    return jobid


def queryJobStatus(id):
    return apiGet(f'job/{id}').get("jobState")


def getQueryResult(query):
    jobId = querySQL(query)
    while queryJobStatus(jobId) != "COMPLETED":
        time.sleep(1)
    return apiGet('job/{id}/results?offset={offset}&limit={limit}'.format(id=jobId, offset=0, limit=100))


response = requests.put('{server}/apiv2/bootstrap/firstuser'.format(server=config.dremioServer),
                        headers=config.get_headers(), data=json.dumps({
        "userName": config.userName,
        "firstName": config.firstName,
        "lastName": config.lastName,
        "createdAt": int(time.time()),
        "email": config.email,
        "password": config.password,
    }))

login()

# https://docs.dremio.com/software/rest-api/sources/sources/

# POSTGRES SOURCES
body = {
    "entityType": "source",
    "name": "catalogue",
    "description": "catalogue data",
    "type": "POSTGRES",
    "config": {
        "username": os.environ.get("POSTGRES_USERNAME"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "hostname": os.environ.get("POSTGRES_HOST"),
        "port": "5432",
        "authenticationType": "MASTER",
        "fetchSize": "0",
        "databaseName": "catalogue_production"
    },
}
print(body)
apiPost('catalog', body=body)

body = {
    "entityType": "source",
    "name": "coproduction",
    "description": "coproduction data",
    "type": "POSTGRES",
    "config": {
        "username": os.environ.get("POSTGRES_USERNAME"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "hostname": os.environ.get("POSTGRES_HOST"),
        "port": "5432",
        "authenticationType": "MASTER",
        "fetchSize": "0",
        "databaseName": "coproduction_production"
    },
}
print(body)
apiPost('catalog', body=body)

# ELASTICSEARCH SOURCE
body = {
    "entityType": "source",
    "name": "elastic",
    "description": "elasticsearch for logs",
    "type": "ELASTIC",
    "config": {
        "username": os.environ.get("ELASTIC_USERNAME"),
        "password": os.environ.get("ELASTIC_PASSWORD"),
        "hostList": [{"hostname": os.environ.get("ELASTIC_HOST"), "port": os.environ.get("ELASTIC_PORT")}],
        "authenticationType": "MASTER",
    },
}
print(body)
apiPost('catalog', body=body)

body = {
    "entityType": "source",
    "name": "elastic2",
    "description": "elasticsearch for logs",
    "type": "ELASTIC",
    "config": {
        "username": os.environ.get("ELASTIC_USERNAME"),
        "password": os.environ.get("ELASTIC_PASSWORD"),
        "hostList": [{"hostname": "elasticsearch", "port": os.environ.get("ELASTIC_PORT")}],
        "authenticationType": "MASTER",
    },
}
print(body)
apiPost('catalog', body=body)

body = {
    "entityType": "source",
    "name": "elastic2",
    "description": "elasticsearch for logs",
    "type": "ELASTIC",
    "config": {
        "username": os.environ.get("ELASTIC_USERNAME"),
        "password": os.environ.get("ELASTIC_PASSWORD"),
        "hostList": [{"hostname": "elasticsearch", "port": os.environ.get("ELASTIC_PORT")}],
        "authenticationType": "MASTER",
    },
}
print(body)
apiPost('catalog', body=body)
