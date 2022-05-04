
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
    make up # will last couple minutes
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