build:
	docker-compose build
up:
	docker-compose up -d
run-debug:
	docker-compose run --rm django
down:
	docker-compose down