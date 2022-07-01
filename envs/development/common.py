import json
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()


class Config():
    userName = os.environ.get("DREMIO_USERNAME", "admin")
    firstName = os.environ.get("DREMIO_USERNAME", "admin")
    lastName = os.environ.get("DREMIO_USERNAME", "admin")
    password = os.environ.get("DREMIO_PASSWORD", "Administr@tor123")
    email = os.environ.get("DREMIO_EMAIL", "interlink@admin.com")
    dremioServer = os.environ.get("DREMIO_SERVER", 'http://localhost:9047')
    token = None

    def get_headers(self):
        if self.token:
            return {'content-type': 'application/json', 'Authorization': '_dremio{authToken}'.format(authToken=self.token)}
        return {'content-type': 'application/json', 'Authorization': '_dremionull'}


config = Config()


def apiGet(endpoint):
    return json.loads(requests.get('{server}/api/v3/{endpoint}'.format(server=config.dremioServer, endpoint=endpoint), headers=config.get_headers()).text)


def apiPost(endpoint, body=None):
    response = requests.post('{server}/api/v3/{endpoint}'.format(server=config.dremioServer,
                                                                 endpoint=endpoint), headers=config.get_headers(), data=json.dumps(body))

    print(response.__dict__)
    text = response.text
    assert response.status_code in [200, 409]

    # a post may return no data
    if (text):
        return json.loads(text)
    else:
        return None


def apiPut(endpoint, body=None):
    return requests.put('{server}/api/v3/{endpoint}'.format(server=config.dremioServer, endpoint=endpoint), headers=config.get_headers(), data=json.dumps(body)).text


def apiDelete(endpoint):
    return requests.delete('{server}/api/v3/{endpoint}'.format(server=config.dremioServer, endpoint=endpoint), headers=config.get_headers())


def login():
    # we login using the old api for now
    loginData = {'userName': config.userName, 'password': config.password}
    response = requests.post(
        '{server}/apiv2/login'.format(server=config.dremioServer), headers=config.get_headers(), data=json.dumps(loginData))
    data = json.loads(response.text)

    # retrieve the login token
    config.token = data['token']


def querySQL(query):
    queryResponse = apiPost('sql', body={'sql': query})
    jobid = queryResponse['id']
    return jobid


def queryJobStatus(id):
    return apiGet(f'job/{id}')


def getQueryResult(query):
    jobId = querySQL(query)
    while queryJobStatus(jobId).get("jobState") != "COMPLETED":
        time.sleep(1)
    return apiGet('job/{id}/results?offset={offset}&limit={limit}'.format(id=jobId, offset=0, limit=100))
