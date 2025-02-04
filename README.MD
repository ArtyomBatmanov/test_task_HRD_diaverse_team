# ТЗ HRD Diaverse team



## Установка и запуск


### Установка зависимостей

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/ArtyomBatmanov/test_task_HRD_diaverse_team
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

### Настройка базы данных

1. Убедитесь, что PostgreSQL установлен и запущен. Создайте базу данных и пользователя. Например, для создания базы данных и пользователя выполните следующие команды в `psql`:

    ```bash
    sudo -u postgres psql
    ```

    Внутри `psql` выполните:

    ```sql
    CREATE DATABASE book_catalog;
    ```



### Настройка Alembic

1. Сгенерируйте файл конфигурации Alembic:

    ```bash
    alembic init alembic
    ```

2. Создайте начальную миграцию и примените её:

    ```bash
    alembic revision --autogenerate -m "initial migration"
    alembic upgrade head
    ```

### Запуск приложения

1. Запустите приложение FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

    `main` - это имя файла, содержащего ваше FastAPI приложение, и `app` - это экземпляр FastAPI внутри этого файла.

2. Откройте веб-браузер и перейдите по адресу `http://127.0.0.1:8000` для доступа к вашему приложению. Вы также можете посетить `http://127.0.0.1:8000/docs` для доступа к автоматически сгенерированной документации API.


### Примечание

1. В условиях ТЗ было сказано, что нужно использовать Celery. Я не совсем понял, где его здесь можно использовать, поэтому не использовал его
2. Также в условиях было сказано "Реализовать Dockerfile для докеризации приложения и docker-compose". Я не смог этого сделать, т.к. был конфликт PostgreSQL и Fastapi. 
Через контейнер PostgreSQL не запускается на localhost, как правило используется порт 5432. Но в таком случае не запускается Fastapi сервер, просто идёт бесконечная загрузка. Я не смог решить эту проблему

