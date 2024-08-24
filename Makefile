.PHONY: build up stop venv

build:
	docker-compose build

up:
	docker-compose up --build

stop:
	docker-compose down

venv:
	python3 -m venv .venv