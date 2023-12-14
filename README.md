<h1> Проект по тестированию сайта Positive Technologies</h1>

> <a target="_blank" href="https://www.ptsecurity.com/ru-ru/">Ссылка на сайт</a>

![Homepage](image/Homepage.png)

### Используемый стэк

<img title="Python" src="./image/python.png" height="40" width="40"/> <img title="Pytest" src="./image/pytest.png" height="40" width="40"/> <img title="Pycharm" src="./image/pycharm.png" height="40" width="40"/> <img title="Selenium" src="./image/selenium.png" height="40" width="40"/> <img title="Selene" src="./image/selene.png" height="40" width="40"/> <img title="Jenkins" src="./image/jenkins.png" height="40" width="40"/> <img title="GitHub" src="./image/github.png" height="40" width="40"/> <img title="Allure Report" src="./image/allure_report.png" height="40" width="40"/> <img title="Allure TestOps" src="./image/allureTestOps.png" height="40" width="40"/><img title="Telegram" src="./image/telegram.png" height="40" width="40"/> 

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/test-qa_guru_15/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

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

![Allure_report_example](./image/Allure_report_example.png)

#### Список тест кейсов

![Allure_suites](./image/Allure_suites.png)

#### Отчет прохождения теста

![Allure_suites_test](./image/Allure_suites_test.png)

#### Графики прохождения тестов

![Allure_graphs](./image/Allure_graphs.png)

### Оповещения в Telegram

![allert_bot](./image/allert_bot.png)