from .google import service, sheet_id
from datetime import datetime
from common import *
import json

login()

queries = [
    # coproductionprocesses
    {
        "name": "Number of coproduction processes",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess",
        "extract_count": True
    },
    {
        "name": "Number of coproduction processes in english",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.language LIKE 'en",
        "extract_count": True
    },
    {
        "name": "Number of coproduction processes in latvian",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.language LIKE 'lv",
        "extract_count": True
    },
    {
        "name": "Number of coproduction processes in italian",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.language LIKE 'it",
        "extract_count": True
    },
    {
        "name": "Number of coproduction processes in spanish",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.language LIKE 'es",
        "extract_count": True
    },
    # permissions
    {
        "name": "Number of permissions",
        "sql": "SELECT COUNT(*) FROM coproduction.public.permission",
        "extract_count": True
    },
    # teams
    {
        "name": "Number of teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team",
        "extract_count": True
    },
    {
        "name": "Number of public administration teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'public_administration'",
        "extract_count": True
    },
    {
        "name": "Number of public administration teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration'",
        "extract_count": True
    },
    {
        "name": "Number of citizen teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'citizen'",
        "extract_count": True
    },
    {
        "name": "Number of citizen teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen'",
        "extract_count": True
    },
    {
        "name": "Number of TSO teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE '%organization%'",
        "extract_count": True
    },
    {
        "name": "Number of TSO teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "extract_count": True
    },
    # organizations
    {
        "name": "Number of organizations",
        "sql": "SELECT COUNT(*) FROM coproduction.public.organization",
        "extract_count": True
    },
    # assets
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
    # users
    {
        "name": "Number of users",
        "sql": "SELECT COUNT(*) FROM coproduction.public.\"user\"",
        "extract_count": True
    },
    {
        "name": "Number of public servants",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'public_administration' )",
        "extract_count": True
    },
    {
        "name": "Number of public servants involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration' )",
        "extract_count": True
    },
    {
        "name": "Number of citizens",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'citizen' )",
        "extract_count": True
    },
    {
        "name": "Number of citizens involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen' )",
        "extract_count": True
    },
    {
        "name": "Number of TSO users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE '%organization%' )",
        "extract_count": True
    },
    {
        "name": "Number of TSO users involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%' )",
        "extract_count": True
    },

]

results = run_queries(queries)

# print(json.dumps(results))

ENVIRONMENT = os.environ.get("PLATFORM_STACK_NAME")

# send data to GoogleDrive

try:
    result = service.spreadsheets().values().get(spreadsheetId=sheet_id,
                                                 range=f"{ENVIRONMENT}!A1:ZZ1").execute()
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
    spreadsheetId=sheet_id,
    range=f"{ENVIRONMENT}!A:Z",
    body={
        "majorDimension": "ROWS",
        "values": values
    },
    valueInputOption="USER_ENTERED"
).execute()

print(
    f"Document updated. See it at: https://docs.google.com/spreadsheets/d/{sheet_id}")
