# Weblate for continous localization

Weblate is a libre web-based translation tool with tight version control integration. It provides two user interfaces, propagation of translations across components, quality checks and automatic linking to source files.

## How to use weblate
https://docs.google.com/document/u/2/d/1GApY_q1txqRJeYgQ_pZk01WG5XZXl38R-VyLXpIh3t4/edit

## Deployment of weblate

Weblate is deployed only in the demo environment. You can find its docker-compose in the interlink-project repository:

https://github.com/interlink-project/interlink-project/tree/master/envs/internationalization

```sh
cd /datadrive/data/interlink-project/envs/internationalization
docker-compose up -d
```

## Components in weblate

### Collaborative environment frontend component

* Translation files come from: https://github.com/interlink-project/frontend/tree/master/react/src/translations

* Weblate project: https://demo.interlink-project.eu/weblate/projects/collaborative-environment/frontend/

### Seeding data component

* Translation files come from: https://github.com/interlink-project/interlinkers-data/tree/master/weblate
* Weblate project: https://demo.interlink-project.eu/weblate/projects/seeding-data/