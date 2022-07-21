## Errors

### AuthorizationException(403, 'cluster_block_exception', 'blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];')

Go to backend-logging and:

apt get update && apt get upgrade
apt install curl
curl --user ELASTIC_USER:ELASTIC_PASSWORD -X PUT http://elasticsearch:9200/logs/_settings -H 'Content-Type: application/json' -d '{ "index": { "blocks": { "read_only_allow_delete": "false" } } }'