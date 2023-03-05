up:
	docker-compose -f docker-compose.dev.yml up -d --build
down:
	docker-compose -f docker-compose.dev.yml down --rmi local