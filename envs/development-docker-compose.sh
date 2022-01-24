
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env "$@"