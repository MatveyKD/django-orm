# Пульт охраны банка
Пульт охраны банка со списком активных карт доступа, списком людей в хранилище и списком посещений опреленного человека.

## Как установить
Python3 должен быть уже установлен. Затем используйте pip для установки зависимостей:

    pip install -r requirements.txt

### Переменные окружения
Чтобы указать переменные окружения (необходимые для работы), создайте в изначальной папке файл `.env`. Его содержимое должно быть похожим на это:

    ENGINE=django.db.backends.postgresql_psycopg2
    HOST=checkpoint.host.example
    PORT=7492
    NAME=checkpoint
    USER=guard
    PASSWORD=kvob1
    LANGUAGE_CODE=ru-ru
    TIME_ZONE=Europe/Moscow
    BACKEND=django.template.backends.django.DjangoTemplates
    DEBUG=False

`ENGINE` - движок для сайта. Указанный в примере работает.\

`HOST` - хост базы данных.

`PORT` - порт

`NAME` - имя пользователя.

`USER` - никнейм пользователя.

`PASSWORD` - пароль пользователя.

`LANGUAGE_CODE` - код языка для вашего пульта.

`TIME_ZONE` - Часовой пояс для вашего пульта. В примере используется пояс Москвы.

`BACKEND` - бэкенд django. Указанный в примере работает.

`DEBUG` - дебаг режим. Включается значением `True`, выключается значением `False`.

## Пример успешной работы

При успешном запуске скрипта по адресу `http://127.0.0.1:8000/` появится пульт охраны, а в терминал выведится это:
    
    PS C:\Users\hp\django-orm> python manage.py runserver 0.0.0.0:8000
    Performing system checks...
    
    System check identified no issues (0 silenced).
    June 09, 2022 - 13:39:20
    Django version 3.2.13, using settings 'project.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CTRL-BREAK.
