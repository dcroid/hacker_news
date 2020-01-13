**Тестовое задание** 

Приложение для периодической выгрузки новостей с главной страницу Hacker News  и сохрание новостей в базу данных.

---
**Установка**

На компьюте должен быть установлен docker и docker-composer

**Установка (инициализация) приложения**

``chmod +x init.sh``

``./init.sh`` 


**Запуск приложения**
``docker-compose up -d``

**Остановка приложения**
``docker-compose stop``

**Ручной запуск парсера**
``docker exec -it hacker_news_app ./scripts/get_news.sh``

По умолчинию celery beat отправляется задачу каждый час, для того, что бы изменить переодичность отправки задачи на выгрузку
необходимо изменить парамет BEAT_PERIOD в .env

---

**Работа с API**

Получить главной страницу 
``curl -X GET http://localhost:8000/posts``

Пример ответа:
``{"count":60,"next":"http://localhost:8000/posts?limit=5&offset=5","previous":null,"results":[{"id":31,"title":"Bug #915: Please help","url":"https://nedbatchelder.com/blog/202001/bug_915_please_help.html","created":"2020-01-12T20:49:55.930712Z"},{"id":32,"title":"Bash $* and $@ (2017)","url":"https://eklitzke.org/bash-$%2A-and-$@","created":"2020-01-12T20:49:55.930782Z"},{"id":33,"title":"Don't just roll the dice – Software pricing guide [pdf]","url":"https://neildavidson.com/downloads/dont-just-roll-the-dice-2.0.0.pdf","created":"2020-01-12T20:49:55.930815Z"},{"id":34,"title":"Rust DataBase Connectivity (RDBC)","url":"https://andygrove.io/2020/01/rust-database-connectivity-rdbc/","created":"2020-01-12T20:49:55.930847Z"},{"id":35,"title":"Deploy your side-projects at scale for basically nothing – Google Cloud Run","url":"https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless","created":"2020-01-12T20:49:55.930880Z"}]}``

Сортировка по полям
``curl -X GET http://localhost:8000/posts?order=title``

для сортировки доступны след. поля: id, title, url, created

Смещения и лимиты:
``curl -X GET http://localhost:8000/posts?offset=10&limit=10``

доступны след. параметры: offset и limit