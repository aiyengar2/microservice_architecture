# microservice_architecture

Run ./begin.sh to start up the docker containers and ./end.sh to end them.

You must have Docker installed and have the daemon running before you run ./begin.sh.

This will create two webservers on localhost:8000 (UI) and localhost:5000 (DB), where:

localhost:8000 - displays a basic Hello World

localhost:5000/info - displays some basic JSON that serves as a model for our DB

localhost:8000/info - queries our "DB" at localhost:5000/info and displays an html template with the result of our DB call embedded
