#!/usr/bin/env bash

pip3 install -r /opt/jobs/requirements.txt 
python 3 /opt/jobs/dremio/setup.py

/sbin/tini -- /docker-entrypoint crond -f