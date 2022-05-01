
# CI/CD policies for INTERLINK software

## Continuous Integration (CI)

### Unit Tests (UT)

Every SW package should have Unit Tests (UT) provided by SW package authors.
Project DevOps should configure automatic workflow to execute those UT on every push to master branch.

### SW Releases

Once a SW component archieves an important implementation milestone by developers, its code should be TAGged.
For SW version which are intended for deployment, a SW release should be built per each SW repository.
Either assigning a TAG or having built a SW release should trigger automatic building of a new docker image(s) for this SW repository.
Docker images should contain TAG or SW version somewhere in the name of the docker image.

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
