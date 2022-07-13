from datetime import datetime
from common import *
import json

login()

queries = [
    {
        "name": "Number of coproduction processes",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess",
        "extract_count": True
    },
    {
        "name": "Number of permissions",
        "sql": "SELECT COUNT(*) FROM coproduction.public.permission",
        "extract_count": True
    },
    {
        "name": "Number of teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team",
        "extract_count": True
    },
    {
        "name": "Number of organizations",
        "sql": "SELECT COUNT(*) FROM coproduction.public.organization",
        "extract_count": True
    },
    {
        "name": "Number of assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.asset",
        "extract_count": True
    },
    {
        "name": "Number of external assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.externalasset",
        "extract_count": True
    },
    {
        "name": "Number of internal assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.internalasset",
        "extract_count": True
    },
    {
        "name": "Number of interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.interlinker",
        "extract_count": True
    },
    {
        "name": "Number of knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.knowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "Number of software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.softwareinterlinker",
        "extract_count": True
    },
    {
        "name": "Number of external software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.externalsoftwareinterlinker",
        "extract_count": True
    },
    {
        "name": "Number of external knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.externalknowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "Used software interlinkers",
        "sql": "SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)",
    },
    {
        "name": "Used knowledge interlinkers",
        "sql": "SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)",
    },
    {
        "name": "Used external interlinkers",
        "sql": "SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.externalasset.externalinterlinker_id) FROM coproduction.public.externalasset)",
    },
    {
        "name": "Number of used software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)",
        "extract_count": True
    },
    {
        "name": "Number of used knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)",
        "extract_count": True
    },
    {
        "name": "Number of used external interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.externalasset.externalinterlinker_id) FROM coproduction.public.externalasset)",
        "extract_count": True
    },
    {
        "name": "Number of users",
        "sql": "SELECT COUNT(*) FROM coproduction.public.\"user\"",
        "extract_count": True
    },
    # public servants
    {
        "name": "Number of public servants",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'public_administration' )",
        "extract_count": True
    },    
    {
        "name": "Number of public administration teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'public_administration'",
        "extract_count": True
    },    
    {
        "name": "Number of public servants involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration' )",
        "extract_count": True
    },   
    {
        "name": "Number of public administration teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration'",
        "extract_count": True
    },   
    # citizens
    {
        "name": "Number of citizens",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'citizen' )",
        "extract_count": True
    },    
    {
        "name": "Number of citizen teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'citizen'",
        "extract_count": True
    },    
    {
        "name": "Number of citizens involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen' )",
        "extract_count": True
    },   
    {
        "name": "Number of citizen teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen'",
        "extract_count": True
    },  
    # TSO
    {
        "name": "Number of TSO users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE '%organization%' )",
        "extract_count": True
    },    
    {
        "name": "Number of TSO teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE '%organization%'",
        "extract_count": True
    },    
    {
        "name": "Number of TSO users involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%' )",
        "extract_count": True
    },   
    {
        "name": "Number of TSO teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "extract_count": True
    },        
]

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

while len(jobs) > 0:
    time.sleep(1)

    unfinished_jobs = {}
    for job_data in jobs:
        jobId = job_data.get("jobid")
        if queryJobStatus(jobId) == "COMPLETED":
            # get the result of the query
            res = apiGet('job/{id}/results?offset={offset}&limit={limit}'.format(id=jobId, offset=0, limit=100))
            
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
    print(len(unfinished_jobs), "jobs remaining")

# print(json.dumps(results))

ENVIRONMENT = os.environ.get("PLATFORM_STACK_NAME")

# send data to GoogleDrive

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_dict({
  "type": "service_account",
  "project_id": "interlink-deusto",
  "private_key_id": "d92f5cdc7a80cf76bd7b0f7733d3343ab16cba32",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDW/hXd9Qum1UTz\n/KGfjPdsdSUV2b4XE0t6DTseGt3eK8CzlqlqouseP7/AWe3IMuSmxTh7Tako3C4f\nS51GHgAI+Lv1oB9mK5kD70H9xryt8vRo+ET5mgZ7YrIvNmUqBBwfURofb7ik17zc\nacAD55qQYNeLPRYWFuoyCrXMkiF3rWRyZGyJDGzIJil6fDMsrpIQVbl7RdKZUWWB\nfBnNC1m7VfuPF/izuf68i6iOBovNIKcZiKVkVypm75WSwAmw+WdiyoF8SuJXy/EJ\npoYsonjoqcIjyshwGaHwpaKZWLLUK8iIawaT90FWN7HFuhXbOBQa0sWiYK4ismdc\nIOUNWTbNAgMBAAECggEADdj4lTIVYAq++Dm+oN8DIl861kXbsozLNCW20XrIugJD\nbs3QRIGqqmlP80m99EK8hRyRRY/il2Xz91wQpm8d1w+xiGHNFyQAi3pVQjOsyRKr\n0p8H6LPJ1LF7HJz6T+x+Pmrw4P/gx4bsL544Ge6u/yGqgHNpmsUH39VExG2dIW7r\nBAKwMx0CB4BmvswPd6b66hTVKmKPu5jB1e3FNwbeRWo+D/8K+6/7DBJcj0Fnor+a\n+6SmsIlXjF/LrLWmNMUWOhQ/VRKh5J5d7XkDAwlBvIruU3JhEjkq2fuAd3d7WEfG\nMEangfsgNV65yFiZV7xMAsP+ICQ54/90MBGsmjkLGQKBgQDvvEyT30heG3XIfi28\ntccRZkSTy9bKH0KfrzANvvZSbCqdaXu3+EBDmcUVRmSQQYzhQ833pvsJUpDSkLWw\nIyTE+iRs331v33DJ5I59Yq3QhMAZUUlntcGoRqe7z6ev6dAn0hEdvvIaGuo1BED2\nWUmjsS4se5SzNLHdaHhE4CFnMwKBgQDllA1amo4ojT+DaJJlEHUvuNsSeLLmuT7j\nNJeXa5f4UxenLL+Di2Kd2kdTTyF60f9HTLDbqWrfjOCv9WsiXWF3pKKyHZ4JNZrr\nbiC2uC6jI2rbKPfsCD9cRyQneZ4EKsTnz5oJsChEoIyvAL2NCeXd8rpBbLZ2APan\nhw/ODkLp/wKBgEGB/prZhHjSoBitAepy8XZ7r3mDVandaOMhh8v5xm03SV3CGSBo\nIYdXWVc66PfSMaDMWle1tRsTCKfBCySaNc3tXE6zsx8Cu1svrQ/uCvjTjXpdj+Va\n8RP+Wo8javrStSJscGjkaFthx2W9R9MJCupD3A4jprphR8jsZxDK/dWpAoGAVwPu\nq9C44RXoZN5V3oiGYjgmkLG+3USJWYStkG7vgue7p1mGnU1Pa5U4Q5NSlULTBytC\nPX/RSjoTT54tpTDPqJF2ORyQsdzngySSsa7NvnfGIJs+nO/jVA6C3ZNzGRE84MAH\nGnTyTlCsAgi9z59YyO8fOX0DC2cCFi1TCD7PjfECgYEAsdpQ2BIGOuz3NKLzzLwA\nS76ANqJZfLQMeZ/8qiDWDlaGTiwIahV9WtEYPY7tr1vIXKA6znC0iHrYzP5Fkvi/\n3o2UkAF/6Crf9tOzEahsHQSm8242YwGtB8g1KJF5ZnjA/fg1u0wEnJuiLTS6UEav\nCKGdcHJR2t5I//qz3IYmXmg=\n-----END PRIVATE KEY-----\n",
  "client_email": "kpis-106@interlink-deusto.iam.gserviceaccount.com",
  "client_id": "116674489579363548648",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/kpis-106%40interlink-deusto.iam.gserviceaccount.com"
}
, SCOPES)


service = build('sheets', 'v4', credentials=credentials)
driveservice = build('drive', 'v3', credentials=credentials)

id = "1WDA5hatG7NLCzBTpIoVFM_yiRU_Nn6kTsbeYyPXs03A"
if not id:
    spreadsheet = {
        'properties': {
            'title': "KPI results"
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
    user_permission = {
            'type': 'anyone',
            'role': 'writer',
        }
    perm = driveservice.permissions().create(
            fileId=spreadsheet.get('spreadsheetId'),
            body=user_permission,
            fields='id',
        ).execute()

    id = spreadsheet.get('spreadsheetId')
try:
    result = service.spreadsheets().values().get( spreadsheetId=id, range=f"{ENVIRONMENT}!A1:ZZ1").execute()
    header = result.get('values', [[]])
except:
    header = [[]]

values = []
# if there are no rows, sheet is empty, so create header with kpis names
should_be_header = ["Date time"] + [key for key, value in results.items()]
if header[0] != should_be_header:
    values.append(
        should_be_header
    )

# date in the left cell
date_time = datetime.now()
str_date = date_time.strftime("%Y-%m-%d %H:%M:%S")

values.append(
    [str_date] + [json.dumps(value) for key, value in results.items()]
)
    
service.spreadsheets().values().append(
        spreadsheetId=id,
        range=f"{ENVIRONMENT}!A:Z",
        body={
            "majorDimension": "ROWS",
            "values": values
        },
        valueInputOption="USER_ENTERED"
    ).execute()

print(f"Document updated. See it at: https://docs.google.com/spreadsheets/d/{id}")