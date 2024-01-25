<h1> Проект по тестированию сайта Positive Technologies</h1>

> <a target="_blank" href="https://www.ptsecurity.com/ru-ru/">Ссылка на сайт</a>

![Homepage](image/Homepage.png)

### Используемый стэк

<img title="Python" src="./image/python.png" height="40" width="40"/> <img title="Pytest" src="./image/pytest.png" height="40" width="40"/> <img title="Pycharm" src="./image/pycharm.png" height="40" width="40"/> <img title="Selenium" src="./image/selenium.png" height="40" width="40"/> <img title="Selene" src="./image/selene.png" height="40" width="40"/> <img title="Jenkins" src="./image/jenkins.png" height="40" width="40"/> <img title="GitHub" src="./image/github.png" height="40" width="40"/> <img title="Allure Report" src="./image/allure_report.png" height="40" width="40"/> <img title="Jira" src="./image/jira.jpg" height="40" width="40"/> <img title="Allure TestOps" src="./image/allureTestOps.png" height="40" width="40"/><img title="Telegram" src="./image/telegram.png" height="40" width="40"/> 


### Список проверок:
* Проверка наличия баннеров на главной странице
* Проверка поп-ап окна с согласием на использование cookies
* Проверка возвращения на главную страницу через логотип компании
* Проверка перехода на страницу с вакансиями
* Проверка работы фильтра по направлению вакансии
* Проверка открытия детальной информации по вакансии 
* Проверка неуспешной авторизации

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/test-qa_guru_15/">Ссылка на проект в Jenkins</a>

Наш проект возможно запускать через Jenkins. Доступны следующие параметры сборки:
* `environment` - параметр позволяет выбрать окружение, на котором будут запущены тесты
* `comment` - параметр позволяет выбрать комментарий из предложенных


#### Шаги для запуска автотестов через Jenkins

1. Открыть страницу <a target="_blank" href="https://jenkins.autotests.cloud/job/test-qa_guru_15/">проекта</a>
2. В меню выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Выбрать комментарий
5. Нажать кнопку `Build`

После прохождения автотестов в Build History будет доступен отчет

![Jenkins build](./image/jenkins_build.png)

----

### Allure отчет
#### Общие результаты

На странице с общими результатами мы можем увидеть общее количество тестов, сколько из них были успешными и сколько не успешными

![Allure_report_example](./image/Allure_report_example.png)

#### Отчет прохождения теста

В отчете для каждого кейса доступны 4 приложения. Среди них видеофиксация тест-кейса, скриншот, логи и html страницы

![Allure_suites_test](./image/Allure_suites_test.png)

#### Графики прохождения тестов

На странице с графиками мы можем проанализировать наши запуски

![Allure_graphs](./image/Allure_graphs.png)

----

### Интеграция с Jira

![Jira_task](./image/jira_task.png)


----

### Интеграция с Allure TestOps

#### Общий список всех кейсов


#### Пример Dashboard с графиками по тест-кейсам

![Dashboard](./image/allure_dashboards.png)

----

### Оповещения в Telegram

После выполнения автотестов, запущенных через Jenkins, также придёт уведомление в Telegram_bot об итогах тестирования

![allert_bot](./image/allert_bot.png)

----

### Видео-пример прохождения теста

![video](./image/video.gif)