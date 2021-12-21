## Interlinkers (interlinkers.docker-compose.yml)
This project is intended to sum up the different interlinkers developed for the project. But, ¿what is an interlinker?

An *interlinker* is a tool that is used to create assets by *instantiating* them. These interlinkers can be classified by its *nature*: **software** or **knowledge**.

* **Software interlinkers** are software based interlinkers. For example, **forum** interlinker can be instantiated to create a forum where users can create channels and send messages. 

* **Knowledge interlinkers** refer to text, slide, spreadsheet or other type of document **templates**, made by someone, that can be "cloned" to be modified. They use one of the file backends available, such as **googledrive** or **filemanager**. 

### Regarding software interlinkers... how are they integrated? are all them built with the same technologies?

No. Each interlinker is treated as an independent component, so they can be developed with any framework or tool (MEAN, MERN, django, NextJS... the possibilities are infinite). **The only restriction is to implement an API structure like this:**


## API structure

1. **Create new asset:** POST /*interlinker_name*/api/v1/assets/
1. **Get existing asset:** GET /*interlinker_name*/api/v1/assets/{id}
1. **Update existing asset:** PUT /*interlinker_name*/api/v1/assets/{id}
1. **Delete existing asset:** DELETE /*interlinker_name*/api/v1/assets/{id}
1. **Clone existing asset:** POST /*interlinker_name*/api/v1/assets/{id}/clone
1. **Show interlinker GUI for specified asset:** GET /*interlinker_name*/api/v1/assets/{id}/gui

Ideally, these interlinkers have to expose an specifically structured API, which runs business logic for their operation and a user interface that will be integrated through iframes in the main frontend.



### Interlinkers list:

* **forum**:
  * Functionality: allows users to create channels and send messages through them. 
  * Asset meaning: *forum room* where channels can be created.
  * GUI demo ( /forum/api/v1/assets/{id}/gui ):

    ![Forum gui](/images/interlinkers/forum.png)

    And its integration in the main frontend with an iframe:

    ![Forum integration](/images/interlinkers/forumintegration.png)


  * Docs: http://localhost/forum/docs

* **voting tool** (NOT IMPLEMENTED YET):
  * Functionality: allows users to vote. 
  * Asset meaning: *voting* where users can vote for an option.
  * GUI demo:
  * Docs: 

* **repository** (NOT IMPLEMENTED YET):
  * Functionality: allows users to store files in a repository (collection of files) using file backends (next section). 
  * Asset meaning: *repository* where files can be managed.
  * GUI demo:
  * Docs: 

### Data
* **mongodb**: NoSQL database for all interlinkers


## File backends (filebackends.docker-compose.yml)

Similar to interlinkers, these components expose an API (with the same structure) to store files. Instead, they do not provide a GUI endpoint.

1. **Create new asset:** POST /*interlinker_name*/api/v1/assets/
1. **Get existing asset:** GET /*interlinker_name*/api/v1/assets/{id}
1. **Update existing asset:** PUT /*interlinker_name*/api/v1/assets/{id}
1. **Delete existing asset:** DELETE /*interlinker_name*/api/v1/assets/{id}
1. **Clone existing asset:** POST /*interlinker_name*/api/v1/assets/{id}/clone

* **googledrive**:
  * Functionality: stores files in Google Drive.
  * Asset meaning: *file* stored in Google Drive. Can be word, slides or spreadsheet
  * Docs: http://localhost/googledrive/docs

* **filemanager**:
  * Functionality: stores files in AWS S3.
  * Asset meaning: *file* stored in file directory (in future may be integrated with AWS S3 buckets)
  * Docs: http://localhost/filemanager/docs

* **gitmanager** (NOT IMPLEMENTED YET):
  * Functionality: stores files in github repositories, being able to see versions (commits) and the diffs.
  * Asset meaning: GitHub repository.
  * Docs: 

  ![File backends](/images/filebackends.png)
