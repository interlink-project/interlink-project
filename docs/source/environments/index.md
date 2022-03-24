
# Setup local development environment

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
    ![Setup](images/setup.gif)
    
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
