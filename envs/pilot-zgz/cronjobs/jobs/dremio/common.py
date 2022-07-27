import json
import requests
import os
import time

class Config():
    userName = os.environ.get("DREMIO_USERNAME")
    firstName = os.environ.get("DREMIO_USERNAME")
    lastName = os.environ.get("DREMIO_USERNAME")
    password = os.environ.get("DREMIO_PASSWORD")
    email = os.environ.get("DREMIO_EMAIL", "interlink@admin.com")
    dremioServer = "http://dremio:9047"
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
    # print(response.status_code, text)
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
    return apiGet(f'job/{id}').get("jobState")


def getQueryResult(query):
    jobId = querySQL(query)
    while queryJobStatus(jobId) != "COMPLETED":
        time.sleep(1)
    return apiGet('job/{id}/results?offset={offset}&limit={limit}'.format(id=jobId, offset=0, limit=100))

MAX_ITERATIONS = 10

def run_queries(queries):
    results = {}
    jobs = []

    for query_data in queries:
        name = query_data.get("name")
        sql = query_data.get("sql")
        extract_count = query_data.get("extract_count", False)

        jobs.append({
            "jobid": querySQL(sql),
            "name": name,
            "extract_count": extract_count
        })

    iteration = 0
    while len(jobs) > 0 and iteration <= 10:
        time.sleep(1)

        unfinished_jobs = []
        for job_data in jobs:
            jobId = job_data.get("jobid")
            if queryJobStatus(jobId) == "COMPLETED":
                # get the result of the query
                res = apiGet(
                    'job/{id}/results?offset={offset}&limit={limit}'.format(id=jobId, offset=0, limit=100))

                # process the result
                if job_data.get("extract_count"):
                    res = res.get("rows")[0].get('EXPR$0')
                else:
                    res = res.get("rows")

                # set the result
                results[job_data.get("name")] = res
                print("Query '", job_data.get("name"), "' completed!")

            else:
                # add to the unfinished jobs object in order to check it in the next iteration
                unfinished_jobs.append(job_data)

        jobs = unfinished_jobs
        print(len(unfinished_jobs), "jobs remaining", [i.get("name") for i in unfinished_jobs])
        iteration += 1
    return results

def set_list(l, i, v):
    try:
        l[i] = v
    except IndexError:
        for _ in range(i-len(l)+1):
            l.append(None)
        l[i] = v