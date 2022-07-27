#!/usr/bin/env bash

pip3 install -r /opt/jobs/requirements.txt 
/sbin/tini -- /docker-entrypoint crond -f