# Softy

## Описание проекта

Первый проект с использованием Django, который представляет небольшой сайт-блог.  
Реализованный функционал:
- Регистрация и авторизация пользователей
- Публикация и удаление постов
- Просмотр постов с использованием автоподгрузки
- Редактирование своего профиля
- Просмотр чужих профилей

## Используемые технологии

- **Django REST Framework (DRF)**: набор инструментов для создания веб-сервисов и API
- **rest_framework_simplejwt**: аутентификация через JSON Web Tokens (JWT)
- **Django Models**: работа с базой данных
- **PostgreSQL**: СУБД для хранения данных

## Начало работы
### Установка
1. Клонируйте репозиторий:
    ```bash
    git clone github.com/an-lime/Softy_web.git
    cd Softy_web
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

### Запуск
- Переименуйте **.env.example** в **.env** и настройте переменные окружения

- Для работы с базой данных:
    1. Создайте базу в PostgreSQL:
        ```sql
        CREATE DATABASE your_db_name;
        ```
    
    2. Примените миграции:
        ```bash
        python manage.py migrate
        ```

- Запустите сервер:
    ```bash
    python manage.py runserver
    ```