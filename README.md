<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/interlink-project/frontend">
    <img src="docs/images/logo.png" alt="Logo" width="172" height="80">
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

1. Setup the project 

    * linux or macOS: 

    ```sh
    mkdir interlink && cd interlink #Important because "make setup" will create directories on parent
    git clone https://github.com/interlink-project/interlink-project
    cd interlink-project
    make setup
    ```
    ![Setup](docs/images/main/setup.gif)
    
    * windows: *soon*

1. Build all components

    * linux or macOS:
    
    ```sh
    # from interlink-project
    make builddev
    ```

    * windows: *soon*

1. Run all the components integrated

    * linux or macOS: 
    
    ```sh
    # from interlink-project
    make up
    ```

    * windows: *soon*

1. (Optional) Seed databases with data

    * linux or macOS: 
    
    ```sh
    # from interlink-project
    make seed
    ```

    * windows: *soon*

  **How is this done?**

  Take a look at the Makefile and inside component folders; there, you will see three docker-composes:

  1. **docker-compose.yml**: Production ready containers that are attached to the traefik-public network
    
    docker-compose up
  
  would run containers in production mode

  2. **docker-compose.solodev.yml**: overrides main docker-compose file to create development containers for solo-development.  
  
    docker-compose -f docker-compose.yml -f docker-compose.solodev.yml up
  
  would run containers in standalone development mode

  3. **docker-compose.integrated.yml**: overrides main docker-compose file to create development containers that are attached to the traefik-public network (adding traefik labels to enable routing and load balancing)

    docker-compose -f docker-compose.yml -f docker-compose.integrated.yml up 
  
  would run containers in development mode, but implementing *traefik-public* network and labels


## More documentation
* [AUTHENTICATION.md](docs/AUTHENTICATION.md)
* [ARCHITECTURE.md](docs/ARCHITECTURE.md)
* [DATA_MODEL.md](docs/DATA_MODEL.md)
* [INTERLINKERS.md](docs/INTERLINKERS.md)
* [TECHNOLOGIES.md](docs/TECHNOLOGIES.md)
* [MONITORING.md](docs/MONITORING.md)

<p align="right">(<a href="#top">back to top</a>)</p>
