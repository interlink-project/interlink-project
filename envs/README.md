
# Environments

This folder contains the configuration for deploying the development environments.

## Local/base Environment

This is the basic configuration for a local prod-like deployment, that also serves as a basic for the rest of environments.

It deploys the frontend, the services and the databases and makes them accesible at localhost.

```bash
# commands should be executed from this folder (the envs folder)
docker-compose -f base/docker-compose.yml --env-file base/.env pull
docker-compose -f base/docker-compose.yml --env-file base/.env up -d
```

To load initial data:

```bash
docker-compose -f base/docker-compose.yml --env-file base/.env exec catalogue python /app/app/initial_data.py
docker-compose -f base/docker-compose.yml --env-file base/.env exec coproduction python /app/app/initial_data.py
```

To get specific service logs:

```bash
docker-compose -f base/docker-compose.yml --env-file base/.env logs auth
docker-compose -f base/docker-compose.yml --env-file base/.env logs catalogue
```

## Development Environment

This development environment will be kept with the edge of development (main or master branches of all the components). It will be deployed at [dev.interlink-project.eu](https://dev.interlink-project.eu).

The commands for deploying are the following:

```bash
# commands should be executed from this folder (the envs folder)
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env pull
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env up -d
```

Get service status with:

```bash
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env ps
```

To load initial data:

```bash
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env exec catalogue python /app/app/initial_data.py
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env exec coproduction python /app/app/initial_data.py
```

To get specific service logs:

```bash
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env logs auth
docker-compose -f base/docker-compose.yml -f development/docker-compose.dev.yml --env-file development/.env logs catalogue
```
