from dotenv import load_dotenv
from common import *

load_dotenv()

login()

results = {}

def parse_result_of_count_kpi(data):
    return data.get("rows")[0].get('EXPR$0')

res = getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker")
results["Number of interlinkers"] = parse_result_of_count_kpi(res)
res = getQueryResult("SELECT COUNT(*) FROM catalogue.public.knowledgeinterlinker")
results["Number of knowledge interlinkers"] = parse_result_of_count_kpi(res)
res = getQueryResult("SELECT COUNT(*) FROM catalogue.public.softwareinterlinker")
results["Number of software interlinkers"] = parse_result_of_count_kpi(res)
res = getQueryResult("SELECT COUNT(*) FROM catalogue.public.externalinterlinker")
results["Number of external interlinkers"] = parse_result_of_count_kpi(res)

res = getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)")
results["Used software interlinkers"] = parse_result_of_count_kpi(res)
res = getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)")
results["Used knowledge interlinkers"] = parse_result_of_count_kpi(res)
res = getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.externalinterlinker_id) FROM coproduction.public.externalasset)")
results["Used external interlinkers"] = parse_result_of_count_kpi(res)

print(results)