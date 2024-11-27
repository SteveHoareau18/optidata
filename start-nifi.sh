#!/bin/bash
./bin/nifi.sh set-single-user-credentials ${MYSQL_USER} ${NIFI_PASSWORD}
./bin/nifi.sh start