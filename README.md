# Countries Classifier — Классификатор стран
Классификатор стран мира, основанный на "Общероссийском классификаторе стран мира".

## Используемые фреймворки и библиотеки
1. **Django** — "движок" сайта.
2. **django-tables2** — для отображения, пагинации и сортировки таблицы.
3. **django-filter** — для фильтрации.
4. **django-import-export** — для импорта данных (в "админке").
5. **bootstrap5**, **django-crispy-forms** и **crispy-bootstrap5** — визуальное оформление.
6. **htmx** и **django-htmx** — для запросов без перезагрузки страницы.

## Развёртывание
1. Переименовать директорию `env-sample` в `env`. Задать значения переменных окружения в файлах: `.env.dev` и `.env.dev.db` — для разработки; `.env.prod` и `.env.prod.db` — для "продакшна"; `.env.prod.proxy` — для использования с обратным прокси-сервером.
2. Назначение файлов:
- `docker-compose.yml` — разработка
- `docker-compose.prod.yml` — продакшн
- `docker-compose.prod.for-reverse-proxy.yml` — для использования с обратным прокси-сервером

  Выполнить команду:
  ```
  docker compose [-f docker-compose<...>.yml] up -d --build
  ```
3. Применить миграции, создать суперпользователя, собрать статику:
    ```
    docker compose [-f docker-compose<...>.yml] exec web python manage.py migrate
    docker compose [-f docker-compose<...>.yml] exec web python manage.py createsuperuser
    docker compose [-f docker-compose<...>.yml] exec web python manage.py collectstatic
    ```

## Автор
Александр Аравин - [sander-raven](https://github.com/sander-raven). Email: sander-raven@yandex.ru.

## Лицензия
Проект находится под лицензией MIT. Подробнее: смотри файл [LICENSE](LICENSE).
