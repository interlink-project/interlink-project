from elasticsearch import Elasticsearch
import uuid

# pip install elasticsearch==6.8.2
## SCRIPT USED to fix the logs that contained the ids without dashes, which difficulted the cross joins

es = Elasticsearch(
    ['elasticsearch'],
    http_auth=('elastic', 'elastic'),
    scheme="http",
    port=9200,
)

res = es.search(index="logs", body={"size" : 10000, "query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    # print(hit)
    obj : dict = hit["_source"]
    cp = obj.copy()

    # get those values that can be parsed by the UUID constructor and use str() to 
    # dump them to string again, but now without dashes
    for key, value in obj.items():
        try:
            uuid_value = uuid.UUID(value)
            print("Key", key, "contains uuid")
            str_uuid_value = str(uuid_value)
            cp[key] = str_uuid_value
            print("Replaced", value, "with", str_uuid_value)
        except:
            pass
    
    es.update(index="logs", doc_type="log", id=hit["_id"], body={"doc": cp})