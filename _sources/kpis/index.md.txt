# Instructions to retrieve data for KPIs population

INTERLINK needs to feed several KPIs regarding how the co-production process is carried out with the support of the Collaborative Environment and INTERLINKERs and some statistics regarding the teams created, coproduction projects and so on an so forth.

There are two sources from where the designed KPIs can be fed, namely:
1. Queries to INTERLINK Data Model
2. Queries to Grafana Loki where user activity logging is stored

## Exploiting the Data Model
### Endpoints for KPIS

* DEV: https://dev.interlink-project.eu/coproduction/kpis
* DEMO: https://demo.interlink-project.eu/coproduction/kpis
* MEF: https://mef.interlink-project.eu/coproduction/kpis
* ZARAGOZA: https://zgz.interlink-project.eu/coproduction/kpis
* VARAM: https://varam.interlink-project.eu/coproduction/kpis

> The script is located at: 
https://github.com/interlink-project/backend-coproduction/blob/master/coproduction/app/kpis.py

### MANUALLY Querying the INTERLINK Data Model

This section illustrates how to perform queries to the database of co-production exploiting its [data model](https://dev.interlink-project.eu/docs/en/collaborativeenvironment/datamodel/index.html)

The steps to be carried out are:
1. Go to [Portainer](https://www.portainer.io/) front-end for the microservices contenerized in INTERLINK: https://portainer.dev.interlink-project.eu/. Notice that you should change "dev" for the deployment that you want to extract data from. 
2. Log in as	admin / ADMIN_PASSWORD
3. Choose "Containers" in left hand side menu
4. Pick the required container, i.e. `dev-interlink-project-eu-db`
5. Open a >_Console
6. Type in the following command to connect to the database: `psql postgresql://postgres:changethis@localhost:5432`
7. Based on the [Data Model diagram](https://dev.interlink-project.eu/docs/en/collaborativeenvironment/datamodel/index.html) or the tables descriptions returned by Postgres issue queries. 

Check these other schemas to understand better how entities are modelled in INTERLINK:
* [Coproduction DB Schema](https://github.com/interlink-project/backend-coproduction/blob/master/coproduction/dbschema.png)
* [Catalogue DB Schema](https://github.com/interlink-project/backend-catalogue/blob/master/catalogue/dbschema.png)

Some [PLSQL commands](https://www.postgresql.org/docs/current/app-psql.html) which can be useful are documented in article  ["How to List Databases and Tables in PostgreSQL Using psql"](https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/):
* `\\list` or `\\l` to view all of the defined databases on the server, e.g. `\\l`
* `\\connect` or `\\c` to jump between databases, e.g. `\\c sales`
* `\\describe` or `\\dt` to list the tables in a database, e.g.`\\dt`
* `\\d` to figure out internal structure of a table in a database, e.g. `\\d coproductionprocess`

To run a examplary query perform the following commands:
* `\\l`
* `\c coproduction_production`
* `\\dt` to list the tables of DB coproduction_production
* `\\d coproduction_production` to figure out the internal structure of the table
* Run different SQL commands, e.g. `SELECT * FROM coproduction_production`

Alternatively you may execute this single command:
* `psql postgresql://postgres:changethis@localhost:5432/coproduction_production -c 'select * from coproductionprocess';`

## Exploiting the user behaviour logs in INTERLINK
### Issuing queries with Grafana LogQL

Grafana uses its own query language called [LogQL](https://grafana.com/docs/loki/latest/logql/) to query data from [LOKI](https://grafana.com/docs/loki/latest/) o any other source.

There are many tutorials online that be followed to learn LogQL:
* LogQL [documentation](https://grafana.com/docs/loki/latest/logql/)
* [Youtube video](https://www.youtube.com/watch?v=HDpE9v1Syz8) ilustrating how to perform queries over Grafana Loki with LogQL 

Some exemplary queries are illustrated below:
* Count the INTERLINKERs created in a time period
```
sum(count_over_time({container_name=~".*-interlink-project-eu-logging",job="user_loging"}[$interval] | json | (crud="false" or frontend="true") and action="CREATE" and model="ASSET" and external_interlinker="false"))
```
* List the times that distinct knowledge interlinkers have been created
```
sum by (knowledgeinterlinker_name)(count_over_time({container_name=~".*-interlink-project-eu-logging",job="user_loging"}[$interval] | json | (crud="false" or frontend="true") and action="CREATE" and model="ASSET" and external_interlinker="false" and knowledgeinterlinker_name!=""))
```
* List the times that distinct software interlinkers have been instantiated
```
sum by (softwareinterlinker_name)(count_over_time({container_name=~".*-interlink-project-eu-logging",job="user_loging"}[$interval] | json | (crud="false" or frontend="true") and action="CREATE" and model="ASSET" and external_interlinker="false"))
```
* Count the number of co-production processes created
```
sum (count_over_time({container_name=~".*-interlink-project-eu-logging",job="user_loging"}[$interval] | json | (crud="false" or frontend="true") and action="CREATE" model="COPRODPROCESS"))
```
* Count the number of teams created per user 
```
sum by (user_id)(count_over_time({container_name=~".*-interlink-project-eu-logging",job="user_loging"}[$interval] | json | (crud="false" or frontend="true") and action="CREATE" model="TEAM"))
```
Notice the following regarding the above queries: 
* LogQL works not over all existing data (which is stream), but on a data over some period of time, hence the parameter $interval which is used. You should also somehow have it in your queries.
* [json](https://grafana.com/docs/loki/latest/logql/log_queries/#json) parser allows a user to parse and extract labels from the log content
