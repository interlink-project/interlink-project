from dotenv import load_dotenv
from dremio import common

load_dotenv()

common.login()
results = []

results["Number of interlinkers"] = common.getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker")

results["Number of software interlinkers"] = common.getQueryResult("SELECT COUNT(*) FROM catalogue.public.softwareinterlinker")
results["Used software interlinkers"] = common.getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)")
results["Number of used software interlinkers"] = common.getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)")

results["Number of knowledge interlinkers"] = common.getQueryResult("SELECT COUNT(*) FROM catalogue.public.knowledgeinterlinker")
results["Used knowledge interlinkers"] = common.getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)")
results["Number of used knowledge interlinkers"] = common.getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)")

print(results)