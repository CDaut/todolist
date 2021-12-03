# Todolist

I couldn't find a Todolist app that would satisfy my criteria so I built this one. This Todolist app should be able to:

- [x] Manage tasks in an eisenhower matrix
- [ ] Be able to dynamically increase task importance based on how long I procrastinated the task
- [x] Manage tasks in different categories
- [x] Have multi user and authentication support
- [ ] Send email notifications
- [ ] Work on mobile to send push notifications
- [ ] Be a PWA

### Stack

This app is built as a progressive web app (pwa). In the backend it uses Django, in the frontend it uses the materialize
framework. Because of the docker-compose setup it works with an external PostgreSQL database and is portable.

### Setup

1. Change the credentials in enviroment.env . This file is on GitHub! Use a generator like https://djecrety.ir/ to
   generate a Django secret key.
2. Run `docker-compose up` to start database and webserver container. This may fail if ran for the first time because of
   some database issues that aren't fixed yet. If so, simply stop the containers and rerun the command a second time.
3. Run `docker exec -it <container-name> /bin/bash` to open a terminal into the container.
4. Run `python3 manage.py setupdb` to set up the database with the required default objects.