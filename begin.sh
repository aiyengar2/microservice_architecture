#!/bin/sh

UI_APP=testapp_ui
UI_PORT=8000
UI_PATH=./ui

DB_APP=testapp_db
DB_PORT=5000
DB_PATH=./db

HOST="localhost:"$(ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}')

docker build -t $UI_APP $UI_PATH
# docker run -d -p $UI_PORT:$UI_PORT $UI_APP
docker run --add-host=$HOST -d -p $UI_PORT:$UI_PORT $UI_APP

docker build -t $DB_APP $DB_PATH
docker run -d -p $DB_PORT:$DB_PORT $DB_APP
# docker ps
# docker exec -it 08e0a32d7f89 bash