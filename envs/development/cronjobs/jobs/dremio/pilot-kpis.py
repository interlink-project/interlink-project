from datetime import datetime
from common import *
import json

login()

queries = [
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
        "sql": "SELECT softwareinterlinker_name as NAME, COUNT(softwareinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY softwareinterlinker_name",
    },
    {
        "name": "Used knowledge interlinkers",
        "sql": "SELECT knowledgeinterlinker_name as NAME, COUNT(knowledgeinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY knowledgeinterlinker_name",
    },
    {
        "name": "Number of used software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET'",
        "extract_count": True
    },
    {
        "name": "Number of used knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET'",
        "extract_count": True
    },

]

results = run_queries(queries)

# print(json.dumps(results))

ENVIRONMENT = os.environ.get("PLATFORM_STACK_NAME")

# send data to GoogleDrive
from .google import service, sheet_id

try:
    result = service.spreadsheets().values().get( spreadsheetId=sheet_id, range=f"{ENVIRONMENT}!A1:ZZ1").execute()
    header = result.get('values', [[]])
except:
    header = [[]]

values = []
# if there are no rows, sheet is empty, so create header with kpis names
should_be_header = ["Last update"] + [key for key, value in results.items()]
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
    
service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=f"{ENVIRONMENT}!A2:ZZ2",
        body={
            "majorDimension": "ROWS",
            "values": values
        },
        valueInputOption="USER_ENTERED"
    ).execute()

print(f"Document updated. See it at: https://docs.google.com/spreadsheets/d/{sheet_id}")