# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up test

build:
	docker-compose build

up:
	docker-compose up -d app

down:
	docker-compose down

logs:
	docker-compose logs app | tail -100

test:
	docker exec zebtest_api python -m pytest -v

init_db:
	docker exec zebtest_api flask db init

migrate:
	docker exec zebtest_api flask db migrate

upgrade:
	docker exec zebtest_api flask db upgrade
