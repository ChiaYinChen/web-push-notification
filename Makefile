up:
	docker-compose -f docker-compose.dev.yml up -d
down:
	docker-compose -f docker-compose.dev.yml down --rmi local
build:
	docker-compose -f docker-compose.dev.yml build --no-cache
