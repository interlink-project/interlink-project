
# CI/CD policies for INTERLINK software

## Continuous Integration (CI)

### Unit Tests (UT)

Every SW package should have Unit Tests (UT) provided by SW package authors.
Project DevOps should configure automatic workflow to execute those UT on every push to master branch.

### SW Releases

All INTERLINK SW packages should be grouped into a single INTERLINK SW release, with a way to configure which versions (TAGs) of particular SW packages should be included in given version (TAG) of the INTERLINK SW release. 
For example, INTERLINK SW release version (TAG) 2.1 consists of the following versions (TAGs) per SW package:
- Frontend v1.8
- Backend v3.2
- etc.

### Integration Tests (IT)

Once the entire INTERLINK SW release is tagged, this should trigger execution of Integration Tests (IT) to check compatibility between cross-dependent SW packages within the SW release.

### Building of Docker SW images

Once both UT and IT completed in "green", i.e. on successfull (OK, without errors) termination of UT + IT pipelines, a new pipeline building docker images should launch.

## Environments

There might be the following three environments:
- Local
- DEV
- Staging (= DEMO)

### Local Environment

It is a local computer of a SW package developer. He/she can deploy any versions (branches, tags) of SW there in order to develop his/her SW package. This environment has no docker images autocompiled at GitHub repository, no CI/CD pipelines, etc. and it goes completely under responsibility of particular developer himself/herself.

### Development Environment (DEV)

This environment is used for manual tests of all the SW functionalities, integrations, etc for developers of all the Project SW packages. For this, docker images should be re-built per every new push to master branches by CI pipelines once all UT/IT passed. Once docker image(s) built successfully, CD pipelines are started to deploy those new docker images into DEV server.

### Staging Environment (DEMO)

This environment is used for non-developer members of the project for demonstrations and GUI testing and feedback purposes. For this, docker images are built by CI pipeline out of latest TAGs assigned per every SW package, having all packages passed UT/IT successfully. Once docker images are built out of tagged SW packages, CD pipeline deploys those docker images into Staging Environment server (DEMO).


