import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from helpers.home_page import HomePageHelper
from helpers.universal import UniversalHelper
from helpers.vacancy_page import VacancyPageHelper

home_page = HomePageHelper()
universal_helper = UniversalHelper()
vacancy_page = VacancyPageHelper()


@allure.title("Переход на страницу с вакансиями")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
def test_go_to_vacancy_page():
    with allure.step('Открыть домашнюю страницу'):
        home_page.open_home_page()
    with allure.step('Перейти на страницу списка вакансий'):
        vacancy_page.get_to_vacancy_page()
    with allure.step('Проверить URL страницы'):
        current_url = browser.driver.current_url
        assert "https://www.ptsecurity.com/ru-ru/about/vacancy/" in current_url, \
            f'Текущая ссылка страницы {current_url} не соответствует ожидаемой'


@allure.title("Проверка фильтра по направлению вакансии")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
def test_profession_filters():
    expected_vacancy = 'Информационная безопасность'
    unexpected_vacancy = 'Тестирование'

    with allure.step('Открыть страницу с вакансиями'):
        universal_helper.open_page('/about/vacancy/')
    with allure.step('Выбрать фильтр по направлению деятельности'):
        vacancy_page.choose_filter(expected_vacancy)
    with allure.step('Проверить, что в результатах есть вакансия с указанным направлением'):
        vacancy_page.keyword_appears_in_the_results(expected_vacancy)
    with allure.step('Проверить, что в результатах нет вакансий с другим направлением'):
        vacancy_page.keyword_missing_from_results(unexpected_vacancy)


@allure.title("Проверка открытия страницы с вакансией")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
def test_open_vacancy():
    keyword_1 = 'Мы ищем технического писателя'
    keyword_2 = 'Что мы ожидаем от кандидатов'

    with allure.step('Открыть страницу с вакансиями'):
        universal_helper.open_page('/about/vacancy/')
    with allure.step('Открыть страницу любой вакансии вакансии'):
        vacancy_page.open_vacancy_page('Технический писатель')
    with allure.step('Проверить, что в вакансии присутствуют ключевые слова'):
        vacancy_page.keyword_appears_in_vacancy(keyword_1)
        vacancy_page.keyword_appears_in_vacancy(keyword_2)
