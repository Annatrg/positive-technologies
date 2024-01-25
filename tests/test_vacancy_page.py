import allure
from allure_commons.types import Severity
from selene import browser

from positive_technologies.pages.home_page import HomePage
from positive_technologies.helpers.universal import UniversalHelper
from positive_technologies.pages.vacancy_page import VacancyPage

home = HomePage()
universal = UniversalHelper()
vacancy = VacancyPage()


@allure.title("Переход на страницу с вакансиями")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
def test_go_to_vacancy_page():
    with allure.step('Открыть домашнюю страницу'):
        home.open_home_page()
    with allure.step('Перейти на страницу списка вакансий'):
        vacancy.get_to_vacancy_page()
    with allure.step('Проверить URL страницы'):
        current_url = browser.driver.current_url
        assert "https://www.ptsecurity.com/ru-ru/about/vacancy/" in current_url, \
            f'Текущая ссылка страницы {current_url} не соответствует ожидаемой'


@allure.title("Проверка фильтра по направлению вакансии")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
def test_choose_profession_filters():
    expected_vacancy = 'Информационная безопасность'
    unexpected_vacancy = 'Тестирование'

    with allure.step('Открыть страницу с вакансиями'):
        universal.open_page('/about/vacancy/')
    with allure.step('Выбрать фильтр по направлению деятельности'):
        vacancy.choose_filter(expected_vacancy)
    with allure.step('Проверить, что в результатах есть вакансия с указанным направлением'):
        vacancy.keyword_appears_in_the_results(expected_vacancy)
    with allure.step('Проверить, что в результатах нет вакансий с другим направлением'):
        vacancy.keyword_missing_from_results(unexpected_vacancy)


@allure.title("Проверка открытия страницы с вакансией")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
def test_open_page_about_vacancy():
    keyword_1 = 'Мы ищем технического писателя'
    keyword_2 = 'Что мы ожидаем от кандидатов'

    with allure.step('Открыть страницу с вакансиями'):
        universal.open_page('/about/vacancy/')
    with allure.step('Открыть страницу любой вакансии вакансии'):
        vacancy.open_vacancy_page('Технический писатель')
    with allure.step('Проверить, что в вакансии присутствуют ключевые слова'):
        vacancy.keyword_appears_in_vacancy(keyword_1)
        vacancy.keyword_appears_in_vacancy(keyword_2)
