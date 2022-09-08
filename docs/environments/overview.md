# Local (development) environment 

To get a local copy up and running (http://localhost) follow these simple example steps.

## Prerequisites

* Install [docker-compose](https://docs.docker.com/compose/install/) to run this project.

## Installation

* linux or macOS: 

    ```sh
    # create a parent directory
    mkdir interlink && cd interlink
    # clone the main repository
    git clone https://github.com/interlink-project/interlink-project && cd interlink-project
    # clones all the github repositories in the parent folder
    make setup
    # here you need to create the .secrets files in the backend-auth and interlinker-googledrive folders.
    # start the containers
    make up
    ```

    To STOP all containers:
    ```sh
    # from /interlink-project
    make down
    ```
    ![Setup](images/setup.gif)
    
## Development and Demo

* https://dev.interlink-project.eu
* https://demo.interlink-project.eu


## Pilots (mef / varam / zgz)
* https://mef.interlink-project.eu
* https://varam.interlink-project.eu
* https://zgz.interlink-project.eu



