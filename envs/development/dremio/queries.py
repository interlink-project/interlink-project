from dotenv import load_dotenv
from dremio.functions import login, getQueryResult

load_dotenv()

login()
results = []

results["Number of interlinkers"] = getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker")

results["Number of software interlinkers"] = getQueryResult("SELECT COUNT(*) FROM catalogue.public.softwareinterlinker")
results["Used software interlinkers"] = getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)")
results["Number of used software interlinkers"] = getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.softwareinterlinker_id) FROM coproduction.public.internalasset)")

results["Number of knowledge interlinkers"] = getQueryResult("SELECT COUNT(*) FROM catalogue.public.knowledgeinterlinker")
results["Used knowledge interlinkers"] = getQueryResult("SELECT * FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)")
results["Number of used knowledge interlinkers"] = getQueryResult("SELECT COUNT(*) FROM catalogue.public.interlinker WHERE catalogue.public.interlinker.id IN(SELECT DISTINCT(coproduction.public.internalasset.knowledgeinterlinker_id) FROM coproduction.public.internalasset)")

print(results)