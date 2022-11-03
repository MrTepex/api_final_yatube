### API v1 для сервиса YATUBE

Полноценный API для работы с сервисом Yatube.

Позволяет выполнять любые запросы к сайту:
```
- Получение, создание, изменение, удаление публикаций
- Получение, создание, изменение, удаление комментариев
- Получение списка и информации о сообществах
- Подписки на авторов
- Получение JWT-токена
```

Аутентификация производится через JWT-токены.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MrTepex/api_final_yatube
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в приложение yatube_api:

```
cd yapube_api/
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов и ответов на них:

```
Запрос GET:

/api/v1/posts/

Ответ:

{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```
```
Запрос POST:

/api/v1/posts/

Данные запроса:

{
"text": "string",
"image": "string",
"group": 0
}
```
```
Запрос GET:

/api/v1/posts/{id}/

Ответ:

{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```