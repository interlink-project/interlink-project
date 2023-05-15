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

    #  COPRODUCTIONPROCESS

    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A7: Number of coproduction processes",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    # Language es una palabra reservada en Dremio. Hay que ponerlo entre comillas dobles.
    {
        "name": "A7.1: Number of coproduction processes in english",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'en'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A7.2: Number of coproduction processes in latvian",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'lv'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A7.3: Number of coproduction processes in italian",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'it'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A7.4: Number of coproduction processes in spanish",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'es'",
        "extract_count": True
    },

    # PERMISSIONS

    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "Number of permissions",
        "sql": "SELECT COUNT(DISTINCT(permission.id)) FROM coproduction.public.permission",
        "extract_count": True
    },

    # TEAMS

    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A6: Number of teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "Average of members per team",
        "sql": "SELECT AVG(MEMBER_COUNT) FROM ( SELECT team_id, COUNT(*) as MEMBER_COUNT FROM  coproduction.public.association_user_team GROUP BY team_id )",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A6.1: Number of public administration teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team WHERE team.type LIKE 'public_administration'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A6.2: Number of public administration teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A6.3: Number of citizen teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team WHERE team.type LIKE 'citizen'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A6.4: Number of citizen teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    # Los tipos de TSO pueden ser 'Non profit organizations' and 'For profit organizations', por eso buscamos 'organization' en el tipo.
    {
        "name": "A6.5: Number of TSO teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team WHERE team.type LIKE '%organization%'",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A6.6: Number of TSO teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "extract_count": True
    },

    # ORGANIZATIONS

    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A27: Number of organizations",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization",
        "extract_count": True
    },

    # ASSETS

    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A26: Number of assets",
        "sql": "SELECT COUNT(DISTINCT(asset.id)) FROM coproduction.public.asset",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A26.1: Number of external assets",
        "sql": "SELECT COUNT(DISTINCT(externalasset.id)) FROM coproduction.public.externalasset",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    {
        "name": "A26.2: Number of internal assets",
        "sql": "SELECT COUNT(DISTINCT(internalasset.id)) FROM coproduction.public.internalasset",
        "extract_count": True
    },

    # USERS

    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    # User es una palabra reservada en DREMIO, por eso la ponemos entre comillas dobles.
    {
        "name": "Number of users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\"",
        "extract_count": True
    },
    # 12/05/2023 CHECK DANIEL CORRE EN DEMO!!
    # Como existe una variable la consulta probada fué:
    # SELECT COUNT(DISTINCT(user_id)) FROM elastic2.logs.log AS log WHERE log."timestamp" > '2023-04-12'
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
        "name": "A2.1. Number of citizens involved in co-delivered services",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen' INNER JOIN coproduction.public.organization ON team.organization_id = organization.id AND organization.id IN (SELECT coproductionprocess.organization_id FROM coproduction.public.coproductionprocess INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = coproductionprocess.id AND phase.is_part_of_codelivery='true' ) )",
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
        "sql": "SELECT COUNT(DISTINCT(interlinker.id)) FROM catalogue.public.interlinker",
        "extract_count": True
    },
    {
        "name": "A1.1: Number of software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker.id)) FROM catalogue.public.softwareinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.2: Used software interlinkers",
        "sql": "SELECT softwareinterlinker_name as NAME, COUNT(softwareinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY softwareinterlinker_name",
    },
    {
        "name": "A1.3: Number of used software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET'",
        "extract_count": True
    },
    {
        "name": "A1.4: Number of external software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(externalsoftwareinterlinker.id)) FROM catalogue.public.externalsoftwareinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.5: Number of external knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(externalknowledgeinterlinker.id)) FROM catalogue.public.externalknowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.6 Number of external interlinkers",
        "sql": "SELECT COUNT(*) FROM ( SELECT * FROM catalogue.public.interlinker INNER JOIN catalogue.public.externalsoftwareinterlinker ON interlinker.id=externalsoftwareinterlinker.id UNION SELECT * FROM catalogue.public.interlinker INNER JOIN catalogue.public.externalknowledgeinterlinker ON interlinker.id=externalknowledgeinterlinker.id)",
        "extract_count": True
    },
    {
        "name": "A1.8: Number of knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker.id)) FROM catalogue.public.knowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.9: Used knowledge interlinkers",
        "sql": "SELECT knowledgeinterlinker_name as NAME, COUNT(knowledgeinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null GROUP BY knowledgeinterlinker_name",
    },
    {
        "name": "A1.10: Number of used knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null",
        "extract_count": True
    },
    {
        "name": "A3. Number of INTERLINKERs with flag is_sustainabilty related",
        "sql": "SELECT COUNT(DISTINCT(interlinker.id)) FROM catalogue.public.interlinker WHERE interlinker.is_sustainability_related='true'",
        "extract_count": True
    },
    {
        "name": "A9. Number of processes with teams of different stakeholders",
        "sql": "SELECT COALESCE(SUM(counted_coprods),0) FROM (SELECT COUNT(DISTINCT coprod_id) AS counted_coprods  FROM ( SELECT DISTINCT coproductionprocess.id as coprod_id, team.id as team_id, team.type as team_type FROM coproduction.public.coproductionprocess, coproduction.public.team INNER JOIN coproduction.public.permission ON permission.coproductionprocess_id=coproductionprocess.id AND permission.team_id=team.id ORDER BY coproductionprocess.id ) GROUP BY coprod_id HAVING COUNT(DISTINCT team_type)>1)",
        "extract_count": True
    },
    {
        "name": "A10. Number of private companies involved in co-delivered services",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization INNER JOIN coproduction.public.team ON team.organization_id = organization.id AND team.type LIKE '%organization%' AND team.id IN (SELECT permission.team_id FROM coproduction.public.permission INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = permission.coproductionprocess_id AND phase.is_part_of_codelivery='true' )",
        "extract_count": True
    },
    {
        "name": "A12: Number of coproduction processes involved in sustainability",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess_id)) FROM ( SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.internalasset ON asset.id = internalasset.id WHERE knowledgeinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) UNION ALL SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.internalasset ON asset.id = internalasset.id WHERE softwareinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) UNION ALL SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.externalasset ON asset.id = externalasset.id WHERE externalinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) )",
        "extract_count": True
    },
    {
        "name": "A15.1: Number of interlinkers reused in more than one coproduction process",
        "sql": "SELECT COUNT(*) FROM( SELECT knowledgeinterlinker_name, softwareinterlinker_name, COUNT(DISTINCT(coproductionprocess_id)) AS IN_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY knowledgeinterlinker_name, softwareinterlinker_name ) WHERE IN_PROCESSES > 1",
        "extract_count": True
    },

]

print("Obtaining kpis on", str_date)
results = run_queries(queries)

# print(json.dumps(results))

ENVIRONMENT = os.environ.get("PLATFORM_STACK_NAME")

# send data to GoogleDrive
try:
    result = service.spreadsheets().values().get(spreadsheetId=sheet_id,
                                                 range=f"{ENVIRONMENT}!A1:ZZ1").execute()
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
        ["Last value"] +
        [f"=INDICE( FILTER( {char}3:{char} , NO( ESBLANCO( {char}3:{char} ) ) ) , FILAS( FILTER( {char}3:{char} , NO( ESBLANCO( {char}3:{char} ) ) ) ) )" for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
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
