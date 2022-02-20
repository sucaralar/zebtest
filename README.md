#Zebrans Test


A technician test that implements an API with Clean architecture to interact with a catalog of products

### About this
This api is dockerized, it was created with the Flask python framework and the PostgreSQL database was used.

## Getting started

### Prerequisites

- docker: https://docs.docker.com/install/

- docker-compose: https://docs.docker.com/compose/install/

## How does it run?

First you need to clone this awesome project. Once cloned, inside your project folder run:

`docker-compose up -d`

Then run the following command, to initialize the database

`make db`

And voilà! you will have the application working on:

- http://0.0.0.0:5050


## Basic Folder Structure

> application.py

The application declaration file.

> config

Application Configuration files are here.

> models

Declaration of the models that will be used for the project.

> migrations

The use of alembic will give this project a plus when it comes to managing changes in the models. This folder saves the configuration.

> migrations

The use of alembic will give this project a plus when it comes to managing changes in the models. This folder saves the configuration.

> app


This folder has a simple structure based on Clean Architecture with the basic use of Factory Pattern.

> test


Here you can find an example of a unit test, an integration test and a functionality test.

## Live Demo

You can access a live demo at the following link:

- https://zebtest.petwarn.me/

Extra! You can access the postman's documentation at the following link:
- https://documenter.getpostman.com/view/13559058/UVkjwJLF


## Extras
This project has some useful commands in Makefile, like:

- `make build` instead of __docker-compose build__
- `make up` instead of __docker-compose up -d__
- `make down` instead of __docker exec zebtest_api python -m pytest -v__
- `make test` instead of __docker-compose build__
- `make init_db` instead of __docker exec zebtest_api flask db init__
- `make migrate` instead of __docker exec zebtest_api flask db migrate__
- `make upgrade` instead of __docker exec zebtest_api flask db upgrade__
- `make db` to run init_db, migrate and upgrade at the same time




