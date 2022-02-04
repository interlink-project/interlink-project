
# Environments

This folder contains the configuration for deploying the different environments of the INTERLINK project (eventually some might be better moved to a standalone repository).

Each of the folders corresponds to a self-contained environmennt, the folder could be moved or copied to a different location.
The environments do not have dependencies within this repository and download the component images from Docker Hub (in principle images will be public so no authentication is needed).

At least, six different environment configuration will be available for INTERLINK, corresponding to the folders in this repository:

- [**local**](./local) (*WIP - not fully configured or tested yet*): environment for deploying the components of the INTERLINK platform in a local private machine. It does not use SSL/TLS and will be deployed in [localhost](http://localhost). It can be useful as a basis for developing and integrating components. It is expected to match latest development edge (master/main branches of the components) and data is in general not persisted.
- [**development**](./development): integration environment that will be deployed in [dev.interlink-project.eu](https://dev.interlink-project.eu). It is expected to be automarically updated with the latest development edge (master/main branches of the components) and data is in general not persisted and will likely be overwrote with sample default data in each new re-deployment.
- [**demo**](./demo) (*WIP - not configured or tested yet*): central demo or staging environment [demo.interlink-project.eu](https://demo.interlink-project.eu) to demostrate new features and carry out demonstration. In general, data persistence and version stability (no latest images but fixed tagged versions) should be ensured.
- [**pilot-zgz**](./pilot-zgz) (*WIP - not configured or tested yet*): pilot environment [pilot-zgz.interlink-project.eu](https://pilot-zgz.interlink-project.eu). Production-like environment, data persistence and version stability (no latest images but fixed tagged versions) should be ensured.
- [**pilot-mef**](./pilot-mef) (*WIP - not configured or tested yet*): pilot environment [pilot-mef.interlink-project.eu](https://pilot-mef.interlink-project.eu). Production-like environment, data persistence and version stability (no latest images but fixed tagged versions) should be ensured.
- [**pilot-varam**](./pilot-varam) (*WIP - not configured or tested yet*): pilot environment for [pilot-varam.interlink-project.eu](https://pilot-varam.interlink-project.eu). Production-like environment, data persistence and version stability (no latest images but fixed tagged versions) should be ensured.

For now, the environments are deployed in a single machine with Docker Compose. The might change in the future, as well The naming or the URLs of these images might change in the future.

## Requirements

The only software requirement for the deployment of the environment is a working installation of docker and docker-compose (ideally witout the need of using sudo) with support to standard amd64 architecture images (most standard installations would work).

In addition, for the environments that are expected to be publicly available, it is necesary to have a machine with a public IP and to point the corresponding subdomains to the machine public address.

## Environment Deployment

All environments are self-contained and can be deployed using Docker Compose. Each of the folders will eventually contain a `docker-compose.yml` file and one or several environment files with environment varibiables used by the deployment. Special care is required with secrets in production environments. 

One possibility is to define secrets at the level of this repository and refer the corresponding properties in the docker-compose 'environment' settings. In this case it is necessary to explicitly export the secret in the script, e.g., ``export FOO=${{ secrets.BAR }}``.



The deployment and management of the different components is done with standard docker-compose commads executed from the corresponding environment folder in the machine that is expected to host the deploymennt.

The first step is therefore to always move to the environment we are interesting in managing or redeploying.

```bash
# from the folder of this README in the repository
cd <name-of-environment-folder>
# it might be good also to git pull --ff-only the latest version from Github
```

Once we are in the right environment folder, we simply deploy or update the environment to the latest images and configuration (will be read from the folder automatically) with the following commands:

```bash
# commands should be executed from this environment (the envs folder)
docker-compose pull
docker-compose up -d
```

The status of the deployment and services can be checked with:

```bash
docker-compose ps
```

To pre-start and load initial default data for some of the services we can do:

```bash
# pre-start
docker-compose exec catalogue python /app/app/pre_start.py
docker-compose exec coproduction python /app/app/pre_start.py
# load initial data
docker-compose exec catalogue python /app/app/initial_data.py
docker-compose exec coproduction python /app/app/initial_data.py
```

To get specific service logs:

```bash
docker-compose logs <name-of-the-service>
# for example
docker-compose logs auth
docker-compose logs catalogue
```
