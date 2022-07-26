from sheets import service, sheet_id
from datetime import datetime
import dateutil.relativedelta
from common import *
import json

# date in the left cell
date_time = datetime.now()
str_date = date_time.strftime("%Y-%m-%d %H:%M:%S")

d2 = date_time - dateutil.relativedelta.relativedelta(months=1)
one_month_before = d2.strftime("%Y-%m-%d")

login()

queries = [
    # coproductionprocesses
    {
        "name": "A7: Number of coproduction processes",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess",
        "extract_count": True
    },
    {
        "name": "A7.1: Number of coproduction processes in english",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'en'",
        "extract_count": True
    },
    {
        "name": "A7.2: Number of coproduction processes in latvian",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'lv'",
        "extract_count": True
    },
    {
        "name": "A7.3: Number of coproduction processes in italian",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'it'",
        "extract_count": True
    },
    {
        "name": "A7.4: Number of coproduction processes in spanish",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'es'",
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
        "name": "A6: Number of teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team",
        "extract_count": True
    },
    {
        "name": "Average of members per team",
        "sql": "SELECT AVG(MEMBER_COUNT) FROM ( SELECT team_id, COUNT(*) as MEMBER_COUNT FROM  coproduction.public.association_user_team GROUP BY team_id )",
        "extract_count": True
    },
    {
        "name": "A6.1: Number of public administration teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'public_administration'",
        "extract_count": True
    },
    {
        "name": "A6.2: Number of public administration teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration'",
        "extract_count": True
    },
    {
        "name": "A6.3: Number of citizen teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'citizen'",
        "extract_count": True
    },
    {
        "name": "A6.4: Number of citizen teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen'",
        "extract_count": True
    },
    {
        "name": "A6.5: Number of TSO teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE '%organization%'",
        "extract_count": True
    },
    {
        "name": "A6.6: Number of TSO teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "extract_count": True
    },
    # organizations
    {
        "name": "A27: Number of organizations",
        "sql": "SELECT COUNT(*) FROM coproduction.public.organization",
        "extract_count": True
    },
    # assets
    {
        "name": "A26: Number of assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.asset",
        "extract_count": True
    },
    {
        "name": "A26.1: Number of external assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.externalasset",
        "extract_count": True
    },
    {
        "name": "A26.2: Number of internal assets",
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
        "name": "A8: Number of active users last month",
        "sql": f"SELECT COUNT(DISTINCT(user_id)) FROM elastic2.logs.log AS log WHERE log.\"timestamp\" > '{one_month_before}'",
        "extract_count": True
    },
    {
        "name": "A6: Number of public servants",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'public_administration' )",
        "extract_count": True
    },
    {
        "name": "B4: Number of public servants involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration' )",
        "extract_count": True
    },
    {
        "name": "A4: Number of citizens",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'citizen' )",
        "extract_count": True
    },
    {
        "name": "B4: Number of citizens involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen' )",
        "extract_count": True
    },
    {
        "name": "A5: Number of TSO users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE '%organization%' )",
        "extract_count": True
    },
    {
        "name": "B4: Number of TSO users involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%' )",
        "extract_count": True
    },
    # interlinkers
    {
        "name": "A1: Number of interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.interlinker",
        "extract_count": True
    },
    {
        "name": "A1.8: Number of knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.knowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.1: Number of software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.softwareinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.4: Number of external software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.externalsoftwareinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.5: Number of external knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.externalknowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.2: Used software interlinkers",
        "sql": "SELECT softwareinterlinker_name as NAME, COUNT(softwareinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY softwareinterlinker_name",
    },
    {
        "name": "A1.9: Used knowledge interlinkers",
        "sql": "SELECT knowledgeinterlinker_name as NAME, COUNT(knowledgeinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null GROUP BY knowledgeinterlinker_name",
    },
    {
        "name": "A1.3: Number of used software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET'",
        "extract_count": True
    },
    {
        "name": "A1.10: Number of used knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null",
        "extract_count": True
    },
    {
        "name": "A15.1: Number of interlinkers reused in more than one coproduction process",
        "sql": "SELECT COUNT(*) FROM( SELECT knowledgeinterlinker_name, softwareinterlinker_name, COUNT(DISTINCT(coproductionprocess_id)) AS IN_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY knowledgeinterlinker_name, softwareinterlinker_name ) WHERE IN_PROCESSES > 1",
        "extract_count": True
    },
    {
        "name": "A12: Number of coproduction processes involved in sustainability",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess_id)) FROM ( SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.internalasset ON asset.id = internalasset.id WHERE knowledgeinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) UNION ALL SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.internalasset ON asset.id = internalasset.id WHERE softwareinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) UNION ALL SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.externalasset ON asset.id = externalasset.id WHERE externalinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) )",
        "extract_count": True
    },
]

print("Obtaining kpis on", str_date)
results = run_queries(queries)

# print(json.dumps(results))

ENVIRONMENT = os.environ.get("PLATFORM_STACK_NAME")

# send data to GoogleDrive
try:
    result = service.spreadsheets().values().get( spreadsheetId=sheet_id, range=f"{ENVIRONMENT}!A1:ZZ1").execute()
    header = result.get('values', [[]])[0]
except:
    header = []

values_to_insert = []
update = False

if len(header) > 0:
    # check if all query names are present in header and add a new one if not present
    for query in queries:
        name = query.get("name")
        if not name in header:
            header.append(name)
            update = True
            print(f"Added {name} to header")

    # update header if needed
    if update:
        service.spreadsheets().values().update(
            spreadsheetId=sheet_id,
            range=f"{ENVIRONMENT}!A1:ZZ1",
            body={
                "majorDimension": "ROWS",
                "values": [header]
            },
            valueInputOption="USER_ENTERED"
        ).execute()
else:
    # if there are no cells in the header, create them with the kpis names
    header = ["Date time"] + [i.get("name") for i in queries]
    values_to_insert.append(
        header
    )
    values_to_insert.append(
        ["Last value"] + [f"=INDICE( FILTER( {char}3:{char} , NO( ESBLANCO( {char}3:{char} ) ) ) , FILAS( FILTER( {char}3:{char} , NO( ESBLANCO( {char}3:{char} ) ) ) ) )" for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    )

# set each value of row depending on the index of the name of the kpi in the header
row = [str_date]
for query_name, query_result in results.items():
    index = header.index(query_name)
    set_list(row, index, json.dumps(query_result))

values_to_insert.append(
    row
)


# append (the header if necessary) and the row to the existing sheet, defined by ENVIRONMENT (development, demo, zgz...)
service.spreadsheets().values().append(
    spreadsheetId=sheet_id,
    range=f"{ENVIRONMENT}!A:Z",
    body={
        "majorDimension": "ROWS",
        "values": values_to_insert
    },
    valueInputOption="USER_ENTERED"
).execute()

print(
    f"Document updated. See it at: https://docs.google.com/spreadsheets/d/{sheet_id}")
