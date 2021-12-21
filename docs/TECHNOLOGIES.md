

## About technologies used

1. <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">FastAPI</a>:
    * **Where**: 
      * auth, coproduction, users, catalogue, filemanager and googledrive
    * **Why**:
      * **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).
      * **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
      * **Short**: Minimize code duplication. Multiple features from each parameter declaration.
      * **Robust**: Get production-ready code. With automatic interactive documentation.
      * **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> and <a href="http://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.
      * <a href="https://fastapi.tiangolo.com/features/" class="external-link" target="_blank">**Many other features**</a> including automatic validation, serialization, interactive documentation, authentication with OAuth2 JWT tokens, etc.
    * **Used with**:
      * **Alembic** for migrations of the data model (due to relational database usage)
      * **CORS** (Cross Origin Resource Sharing) configured.
      * **Authentication options** (*backend/app/app/core/authentication.py* middleware)
          * Session authentication with cookies (http://localhost/auth/login).
        * Token authentication with bearer token in authorization header.
      * **Pytest** integrated with Docker to test the full API interaction (independent on the database).
      * **Docker Swarm** Mode deployment.
      * **Uvicorn and Gunicorn**: Python web server.
  
1. **NextJS**:
    * **What**: React framework for developing single page Javascript applications.
    * **Where**: 
      * forum
    * **Why**:
      * **Server Side Rendering (SSR)**: This means that once the HTML has been delivered to the client (the user’s browser), nothing else needs to happen for the user to be able to read the content on the page. This makes page loading times appear much faster to the user. Also, it allows to manage data in the serverside, protecting the connection to the database (mongodb) and the logic implemented.
      * **Automatic code splitting**: Next.js is clever enough to only load the Javascript and CSS that are needed for any given page. This makes for much faster page loading times, as a user’s browser doesn't have to download Javascript and CSS that it doesn't need for the specific page the user is viewing. 
      * **Compatibility with MUI**: UI-kit used for the main frontend (built with standard React.js)
      * **Hot Module Replacement (HMR)**: allows developers to see any changes they have made during development, live in the application as soon as they have been made. However, unlike traditional "live reload" methods, it only reloads the modules that have actually changed, preserving the state the application was in and significantly reducing the amount of time required to see changes in action. 

    * **Used with**:
      * **Mongoose**: Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. It manages relationships between data, provides schema validation, and is used to translate between objects in code and the representation of those objects in MongoDB.
      * **Tests**: Pytest


## Next steps

* **i18n**:
  * Pydantic: https://github.com/boardpack/pydantic-i18n?ref=pythonrepo.com
  * Database internationalization: 
    * https://doc-archives.microstrategy.com/producthelp/10.4/ProjectDesignGuide/WebHelp/Lang_1033/Content/ProjectDesign/Internationalization_through_tables_and_columns_or.htm
    * https://medium.com/walkin/database-internationalization-i18n-localization-l10n-design-patterns-94ff372375c6
    * ONLY POSTGRES https://sqlalchemy-utils.readthedocs.io/en/latest/internationalization.html

* https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html

* https://github.com/holgi/fastapi-permissions

* **Event driven**: https://stackoverflow.com/questions/65586853/how-to-use-fastapi-as-consumer-for-rabbitmq-rpc

* **Scaling with traefik**: https://dev.to/entrptaher/part-2-scaling-with-traefik-1k5f
* **Celery broker vs backend**: 
  * https://docs.celeryproject.org/en/stable/getting-started/backends-and-brokers/index.html
  * https://github.com/karthikasasanka/fastapi-celery-redis-rabbitmq
