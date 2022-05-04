
# SW development, CI & CD policies for INTERLINK software

## Continuous Integration (CI)

### Unit Tests (UT)

Every SW package should have Unit Tests (UT) provided by SW package authors.
Project DevOps should configure automatic workflow to execute those UT on every push to master branch.

### SW Releases

Once a SW component archieves an important implementation milestone by developers, its code should be TAGged.
For SW version which are intended for deployment, a SW release should be built per each SW repository based on some existing TAG of the code.
There may be many TAGs on the code (e.g. Monday, Tuesday, etc) and not all of them but some sub-set are intended to become a SW release.
SW release version is usually the same as TAG value or an extended string for example "TAG+additional_suffix".
Having built a SW release should trigger automatic building of a new docker image(s) for this SW repository.
Docker images should contain TAG or SW version somewhere in the name of the docker image, for ex. "image-Interlink-frontend:v3.1".
The deployment of a docker image should be with explicit use of the image (SW release) version suffix "v3.1" instead of just ":latest".


All INTERLINK SW packages should be grouped into a single INTERLINK SW release, with a way to configure which versions (TAGs) of particular SW packages should be included in given version (TAG) of the INTERLINK SW release. For example, INTERLINK SW release version 2.1-zgz consists of the following SW versions per SW package:
- Frontend v1.8
- Backend v3.2
- Zgz module v2.6
- etc.

### Integration Tests (IT)

Once the entire INTERLINK SW release is tagged, this should trigger execution of Integration Tests (IT) to check compatibility between cross-dependent SW packages within the SW release.

### Building of Docker SW images

Once both UT and IT completed in "green", i.e. on successfull (OK, without errors) termination of UT + IT pipelines, a new pipeline building docker images should launch.

Having no UT/IT available, the pipelines to build docker images should be triggered by assignment of TAGs to SW repository or by having built a SW release.

## Continuous Deployment (CD) & Environments

There might be the following SIX environments:
- Local
- DEV
- Staging (= DEMO)
- pilot MEF
- pilot ZGZ
- pilot VARAM

### Local Environment

It is a local computer of a SW package developer. He/she can deploy any versions (branches, tags) of SW there in order to develop his/her SW package. This environment has no docker images autocompiled at GitHub repository, no CI/CD pipelines, etc. and it goes completely under responsibility of particular developer himself/herself.

### Development Environment (DEV)

This environment is used for manual tests of all the SW functionalities, integrations, etc for developers of all the Project SW packages. For this, docker images should be re-built per every new push to master branches by CI pipelines once all UT/IT passed. Once docker image(s) built successfully, CD pipelines are started to deploy those new docker images into DEV server.

### Staging Environment (DEMO)

This environment is used for non-developer members of the project for demonstrations and GUI testing and feedback purposes. For this, docker images are built by CI pipeline out of latest TAGs assigned per every SW package, having all packages passed UT/IT successfully. 
The DEMO server is intended for testing and training sessions with business users, and their work should not be suddenly interrupted by a new docker image deployment. That's why, once the docker images with new staging SW versions are built, DevOps admin should announce to testing users and somehow coordinate with them day and time of deployment of the new SW to the staging (DEMO) server.

### Pilot Servers (ZGZ, MEF, VARAM)

Deployment of INTERLINK SW to pilot servers should contain the common INTERLINK base SW (backend, frontend and other platform type components like DBs, auth, etc) and pilot-specific components (ZGZ SW components for ZGZ pilot, etc.).
The deployment process should be similar to deploying on staging (demo) server.

## Software Updates

### Minor updates (patches)

Minor SW updates are needed when there is either a bug fix or small functionality improvement which (almost) does not affect (of affects very little) other SW components, API interfaces, Data Model, etc. Usually the reason for such SW update appears during SW testing and corresponding issue is created in redmine for corresponding SW component. Fixing the SW code should start a.s.a.p. New SW release with minor version incremented (for ex. 3.2.1) should be created. Deployment should be done on first possible occasion (e.g. over night or a weekend).

Such SW change may happen within the same SW release, for example, during the first pilot demo sessions.

### Major SW updates (new SW release)

Such code update corresponds to implementing a new significant functionality. New SW release should be built and deployed with new major version (e.g. 3.2 or 3.2.0). Usually the new SW release should keep back-compatibility, the same SW design, interfaces, system architecture and data models should be preserved, but could be extended.

Such SW change should happend per different project milestones, for example, there will be initial and final pilot demonstrations with different SW releases.

### SW refactoring

This is very rare case when system architecrue, API interfaces and/or data model are changed significantly or recreated anew. For API this would imply new documentation and testing, for DB this would imply data migration from old DBs into the new ones, with corresponding DB data export and import scriprs, etc.

Such SW changes usually should not happen within the lifetime of the same project. It may happend when a new project is started as a continuation of another one.

## Docker-compose profiling

Docker-compose profiling is a useful mechamism to structure and group lower and upper level SW services within docker-compose YAML file.
It is described in details here: https://docs.docker.com/compose/profiles/

The idea is to try to have separate docker-compose files per each SW service and to include (or exclude) them into the deployment of particular environment.

## Data persistency

For the first pilot demos the configuration data is read out from JSON files stored in GitHub SW repository. The user activity data (new co-production processes, task state changes and asset instances) are kept as long as the DB docker container is not reinstralled. On DB container re-deployment these data may be lost. 

### Current situation

If DB is part of the SW release (e.g. web portal) and requires re-deplyment on re-installation of the web portal, then to allow bugfix SW updates during the pilot demo sessions but at the same time to keep the user activity data, corresponding data export and import should be realized by use of additional data export/import scripts.

### Separation of platfrom SW services

Another approach would be to have low level platform services like DB separated from web portal and other components, so re-deployment of web portal (either backend and/or frontend) should not re-deploy the DB container. In this way, the same DB continues to run keeping the accumulated data.

### Data backups

Backing up data is a goog practice independently on the DB container configuration and re-deployment policies. Having data backed up periodically will save from the global crashes at the level of hosting server, as well as from incidental data loss during e.g. maintenance or other activities. Backed up data should be kept on physically different server, ideally, on different hosting data center location.
