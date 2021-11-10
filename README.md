[![Foodgram_project](https://github.com/Goryunova/foodgram-project-react/actions/workflows/foodgram_project.yml/badge.svg)](https://github.com/Goryunova/foodgram-project-react/actions/workflows/foodgram_project.yml)

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
  ssh praktikum@178.154.246.165
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
  
  * send_message - после сборки и запуска контейнеров происходит отправка сообщения в телеграм об успешном окончании workflow

После выполнения вышеуказанных процедур необходимо установить соединение с сервером:

  ```
  ssh username@server_address
  ```
Стянуть образы с dockerhub и запустить контейнеры

```
sudo docker pull marygor/foodgram-project-react:latest
sudo docker pull marygor/foodgram_frontend:latest
sudo docker-compose up -d
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
  sudo docker exec -it 49ce10d94a33 bash
  ```

Внутри контейнера выполнить миграции:

  ```
  python manage.py migrate
  ```

Создать администратора:
  ```
  python manage.py createsuperuser
  ```
Собрать статику:
  ```
  python manage.py collectstatic
  ```
Далее зайти на сайт под администратором и заполнить таблицы Ингредиенты и Теги 

# Автор:


* [Мария Горюнова](https://github.com/Goryunova)

[Проект доступен по адресу](http://178.154.246.165) (почта: admin@mail.ru, пароль: qwe1937)
