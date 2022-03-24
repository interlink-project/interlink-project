<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/interlink-project/frontend">
    <img src="mddocs/images/logo.png" alt="Logo" width="172" height="80">
  </a>
  <h3 align="center">Interlink collaborative environment orquestrator</h3>

  <p align="center">
    <a href="https://interlink-project.eu/"><strong>View Interlink project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/interlink-project/backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/interlink-project/backend/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About the project

This project is intended to be the orquestrator to create the structure of directories that runs the collaborative environment

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Install [docker-compose](https://docs.docker.com/compose/install/) to run this project.

### Installation

* linux or macOS: 

    ```sh
    mkdir interlink && cd interlink #Important because "make setup" will create directories on parent
    git clone https://github.com/interlink-project/interlink-project && cd interlink-project
    make setup
    ```

    To START all containers:
    ```sh
    # from /interlink-project
    make down # will last couple minutes
    ```

    To STOP all containers:
    ```sh
    # from /interlink-project
    make down
    ```
    ![Setup](mddocs/images/main/setup.gif)
    
1. (Optional) Seed databases with data **can throw errors because we are constantly making changes to the database model**

    * linux or macOS: 
    
    ```sh
    # from /interlink-project
    make seed
    ```

    * windows: *soon*

  **How is this done?**

  Take a look at the Makefile and inside component folders; there, you will see three docker-composes:

  1. **docker-compose.prod.yml**: Production ready containers that are attached to the traefik-public network
    
    docker-compose -f docker-compose.prod.yml up

  2. **docker-compose.devsolo.yml**: run containers in standalone development mode and a database microservice.
  
    docker-compose -f docker-compose.devsolo.yml up
  
  3. **docker-compose.devintegrated.yml**: creates development containers that are attached to the traefik-public network (adding traefik labels to enable routing and load balancing)

    docker-compose -f docker-compose.devintegrated.yml up 


## More documentation
* [CI_CD_policies.md](mddocs/CI_CD_policies.md)
* [INTERLINKERS.md](mddocs/INTERLINKERS.md)
* [AUTHENTICATION.md](mddocs/AUTHENTICATION.md)
* [ROUTING.md](mddocs/ROUTING.md)
* [DATA_MODEL.md](mddocs/DATA_MODEL.md)
* [MONITORING.md](mddocs/MONITORING.md)

<p align="right">(<a href="#top">back to top</a>)</p>
