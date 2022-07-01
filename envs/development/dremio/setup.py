import json
import requests
import time
import os
from dotenv import load_dotenv
from .functions import userName, firstName, lastName, email, password, dremioServer, headers, login, apiPost

load_dotenv()


response = requests.put('{server}/apiv2/bootstrap/firstuser'.format(server=dremioServer), headers=headers, data=json.dumps({
    "userName": userName,
    "firstName": firstName,
    "lastName": lastName,
    "createdAt": int(time.time()),
    "email": email,
    "password": password,
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
        "username": os.environ.get("POSTGRES_USER"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "hostname": os.environ.get("POSTGRES_SERVER"),
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
        "username": os.environ.get("POSTGRES_USER"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "hostname": os.environ.get("POSTGRES_SERVER"),
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
