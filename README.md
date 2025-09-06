# HiTalent API

API-сервис для вопросов и ответов (тестовое задание).

## Стек
- Python 3.12
- Django 5.x
- Django REST Framework
- PostgreSQL
- Docker, Docker Compose
- Pytest

## Установка и запуск

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/Miran1193/hitalent
   cd hitalent
2. Запустить контейнеры:
   ```bash
   docker-compose up -d --build
3. Применить миграции:
   ```bash
   docker-compose exec web python manage.py migrate
4. Запустить тесты:
      ```bash
   docker-compose exec web pytest


Вопросы

POST /questions/ — создать вопрос

GET /questions/ — получить список вопросов

Ответы

POST /answers/ — создать ответ

GET /questions/{id}/answers/ — получить список ответов к вопросу (нужно реализовать)

