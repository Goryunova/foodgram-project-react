# foodgram-project-react

## Описание
«Продуктовый помощник» (Проект Яндекс.Практикум)
Сайт является - базой кулинарных рецептов. Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в txt формате. Также присутствует файл docker-compose, позволяющий , быстро развернуть контейнер базы данных (PostgreSQL), контейнер проекта django + gunicorn и контейнер nginx

# Как запустить
Клонируем проект: 
```
git clone https://github.com/Goryunova/foodgram-project-react.git
```
Для добавления файла .env с настройками базы данных на сервер необходимо:

Установить соединение с сервером по протоколу ssh:

  ```
  ssh username@server_address
  ```

Где username - имя пользователя, под которым будет выполнено подключение к серверу.

server_address - IP-адрес сервера или доменное имя.

Например:

  ```
  ssh praktikum@178.154.241.140
  ```

В домашней директории проекта Создать папку app/:

  ```
  mkdir app
  ```
  
В ней создать папку foodgram-project/:

  ```
  mkdir app/foodgram-project
  
  ```
В ней создать файл .env:

  ```
   sudo touch app/foodgram-project/.env
  ```


Выполнить следующую команду:

  ```
  sudo nano app/foodgram-project/.env
  ```
  
Пример добавляемых настроек:


  ```
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME=postgres
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  DB_HOST=postgres
  DB_PORT=5432
  
  ```

Также необходимо добавить Action secrets в репозитории на GitHub в разделе settings -> Secrets:

* DOCKER_PASSWORD - пароль от DockerHub;
* DOCKER_USERNAME - имя пользователя на DockerHub;
* HOST - ip-адрес сервера;
* SSH_KEY - приватный ssh ключ (публичный должен быть на сервере);
* Опционно:
   ```
  * TELEGRAM_TO - id своего телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
  * TELEGRAM_TOKEN - токен бота (получить токен можно у @BotFather, /token, имя бота)
   ```
# Проверка работоспособности
Теперь если внести любые изменения в проект и выполнить:

  ```
  git add .
  git commit -m "..."
  git push
  ```


Комманда git push является триггером workflow проекта. При выполнении команды git push запустится набор блоков комманд jobs (см. файл main.yaml). Последовательно будут выполнены следующие блоки:
  
  * tests - тестирование проекта на соответствие PEP8 и тестам pytest.

  * build_and_push_to_docker_hub - при успешном прохождении тестов собирается образ (image) для docker контейнера и отправлятеся в DockerHub

  * deploy - после отправки образа на DockerHub начинается деплой проекта на сервере. Происходит копирование следующих файлов с репозитория на сервер:
  
    ```
    1 docker-compose.yaml, необходимый для сборки трех контейнеров:
      1.1 postgres - контейнер базы данных
      1.2 web - контейнер Django приложения + wsgi-сервер gunicorn
      1.3 nginx - веб-сервер
    2 nginx/default.conf - файл кофигурации nginx сервера
    3 static - папка со статическими файлами проекта
    ```

После копировния происходит установка docker и docker-compose на сервере и начинается сборка и запуск контейнеров.

* send_message - после сборки и запуска контейнеров происходит отправка сообщения в телеграм об успешном окончании workflow

После выполнения вышеуказанных процедур необходимо установить соединение с сервером:

  ```
  ssh username@server_address
  ```

Отобразить список работающих контейнеров:

  ```
  sudo docker container ls
  ```

В списке контейнеров копировать CONTAINER ID контейнера username/foodgram-project-react:latest (username - имя пользователя на DockerHub):

  ```
  CONTAINER ID   IMAGE                                   COMMAND                  CREATED          STATUS                         PORTS                               NAMES
9901e9fd3f80   nginx:1.19.3                            "/docker-entrypoint.…"   29 seconds ago   Up 26 seconds
49ce10d94a33   marygor/foodgram-project-react:latest   "/entrypoint.sh /bin…"   31 seconds ago   Up 28 seconds
d433369058fd   postgres:13.2                           "docker-entrypoint.s…"   19 hours ago     Restarting (1) 7 seconds ago
  ```

Выполнить вход в контейнер:

  ```
  sudo docker exec -it d3eb395676c6 bash
  ```

Внутри контейнера выполнить миграции:

  ```
  python manage.py migrate
  ```


Также можно наполнить базу данных начальными тестовыми данными:

  ```
  python3 manage.py shell
  >>> from django.contrib.contenttypes.models import ContentType
  >>> ContentType.objects.all().delete()
  >>> quit()
  python manage.py loaddata ingredients.json
  ```
Теперь проекту доступна статика. В админке Django (http://<server_address>/admin) доступно управление данными. Если загрузить фикструры, то будет доступен superuser:

```
  user: Admin
  password: admin
  email: admin@admin.com
```

Для создания нового суперпользователя можно выполнить команду:

  ```
  $ python manage.py createsuperuser
  ```
  
Для остановки и удаления контейнеров и образов на сервере:

  ```
  sudo docker stop $(sudo docker ps -a -q) && sudo docker rm $(sudo docker ps -a -q) && sudo docker rmi $(sudo docker images -q)
  ```

# Автор:


* [Мария Горюнова](https://github.com/Goryunova)

[Проект будет доступен по адресу](http://84.201.163.135) (почта: nikita@reviewer.ru, пароль: test0101)
