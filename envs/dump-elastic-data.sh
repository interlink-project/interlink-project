#!/bin/bash

docker pull elasticdump/elasticsearch-dump

declare -a arr=("logs" "docker" "annotator" "description" "feedback" "filebeat" "survey" "notification")

## now loop through the above array
for i in "${arr[@]}"
do
    echo "Dumping data from index $i"
    docker run --network=dev-interlink-project-eu-default --rm -ti elasticdump/elasticsearch-dump --input=http://elastic:elastic@newelasticsearch:9200/$i --output=http://elastic:elastic@elasticsearch:9200/$i --type=mapping
    docker run --network=dev-interlink-project-eu-default --rm -ti elasticdump/elasticsearch-dump --input=http://elastic:elastic@newelasticsearch:9200/$i --output=http://elastic:elastic@elasticsearch:9200/$i --type=data
done