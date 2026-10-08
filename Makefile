.PHONY: up down run test lint format

up:
	docker compose up -d

down:
	docker compose down

run:
	poetry run uvicorn src.main:app --reload

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .