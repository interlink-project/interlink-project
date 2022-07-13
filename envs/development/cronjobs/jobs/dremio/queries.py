from datetime import datetime
from common import *

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

print(json.dumps(results))

# send data to GoogleDrive

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

GOOGLE_CREDENTIALS = {
        "type": "service_account",
        "project_id":  os.environ.get("GOOGLE_PROJECT_ID"),
        "private_key_id": os.environ.get("GOOGLE_PRIVATE_KEY_ID"),
        "private_key":  os.environ.get("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email":  os.environ.get("settings.GOOGLE_CLIENT_EMAIL"),
        "client_id":  os.environ.get("settings.GOOGLE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/interlinker%40interlink-deusto.iam.gserviceaccount.com"
    }
scope = ['https://www.googleapis.com/auth/spreadsheets']

credentials = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_CREDENTIALS, scope)


service = build('sheets', 'v4', credentials=credentials)

spreadsheet_id = '1Sx8gSmKsvescug4j9QBGr1TH11Ts4hVz05oLr4q9UUc'
columns = [value for key, value in results.items()]

service = build('sheets', 'v4', credentials=credentials)
service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="Sheet1!A:Z",
        body={
            "majorDimension": "COLUMNS",
            "values": columns
        },
        valueInputOption="USER_ENTERED"
    ).execute()