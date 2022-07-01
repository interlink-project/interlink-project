from dotenv import load_dotenv
from common import *

load_dotenv()

login()

# Get attribute can be "rows", "rowCount" or "extract_count"

queries = [
    {
        "name": "Number of coproduction processes",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess",
        "get": "extract_count"
    },
    {
        "name": "Number of permissions",
        "sql": "SELECT COUNT(*) FROM coproduction.public.permission",
        "get": "extract_count"
    },
    {
        "name": "Number of teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team",
        "get": "extract_count"
    },
    {
        "name": "Number of organizations",
        "sql": "SELECT COUNT(*) FROM coproduction.public.organization",
        "get": "extract_count"
    },
    {
        "name": "Number of assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.asset",
        "get": "extract_count"
    },
    {
        "name": "Number of external assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.externalasset",
        "get": "extract_count"
    },
    {
        "name": "Number of internal assets",
        "sql": "SELECT COUNT(*) FROM coproduction.public.internalasset",
        "get": "extract_count"
    },
    {
        "name": "Number of interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.interlinker",
        "get": "extract_count"
    },
    {
        "name": "Number of knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.knowledgeinterlinker",
        "get": "extract_count"
    },
    {
        "name": "Number of software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.softwareinterlinker",
        "get": "extract_count"
    },
    {
        "name": "Number of external software interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.externalsoftwareinterlinker",
        "get": "extract_count"
    },
    {
        "name": "Number of external knowledge interlinkers",
        "sql": "SELECT COUNT(*) FROM catalogue.public.externalknowledgeinterlinker",
        "get": "extract_count"
    },
    {
        "name": "Used software interlinkers",
        "sql": "SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)",
        "get": "rows"
    },
    {
        "name": "Used knowledge interlinkers",
        "sql": "SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)",
        "get": "rows"
    },
    {
        "name": "Used external interlinkers",
        "sql": "SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.externalasset.externalinterlinker_id) FROM coproduction.public.externalasset)",
        "get": "rows"
    },
    {
        "name": "Number of users",
        "sql": "SELECT COUNT(*) FROM coproduction.public.\"user\"",
        "get": "extract_count"
    },
    # public servants
    {
        "name": "Number of public servants",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'public_administration' )",
        "get": "extract_count"
    },    
    {
        "name": "Number of public administration teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'public_administration'",
        "get": "extract_count"
    },    
    {
        "name": "Number of public servants involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration' )",
        "get": "extract_count"
    },   
    {
        "name": "Number of public administration teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration'",
        "get": "extract_count"
    },   
    # citizens
    {
        "name": "Number of citizens",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'citizen' )",
        "get": "extract_count"
    },    
    {
        "name": "Number of citizen teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE 'citizen'",
        "get": "extract_count"
    },    
    {
        "name": "Number of citizens involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen' )",
        "get": "extract_count"
    },   
    {
        "name": "Number of citizen teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen'",
        "get": "extract_count"
    },  
    # TSO
    {
        "name": "Number of TSO users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE '%organization%' )",
        "get": "extract_count"
    },    
    {
        "name": "Number of TSO teams",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team WHERE team.type LIKE '%organization%'",
        "get": "extract_count"
    },    
    {
        "name": "Number of TSO users involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%' )",
        "get": "extract_count"
    },   
    {
        "name": "Number of TSO teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(*) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "get": "extract_count"
    },        
]

results = {}
jobs = []

for query_data in queries:
    name = query_data.get("name")
    sql = query_data.get("sql")
    get = query_data.get("get")

    jobs.append({
        "jobid": querySQL(sql),
        "name": name,
        "get": get
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
            get = job_data.get("get")
            if get in ["rows", "rowCount"]:
                res = res.get(get)
            elif get == "extract_count":
                res = res.get("rows")[0].get('EXPR$0')
            
            # set the result
            results[job_data.get("name")] = res
            print("Query '", job_data.get("name"), "' completed!")
            
        else:
            # add to the unfinished jobs object in order to check it in the next iteration
            unfinished_jobs.append(job_data)

    jobs = unfinished_jobs
    print(len(unfinished_jobs), "jobs remaining")

print(json.dumps(results))

# send data to DB
