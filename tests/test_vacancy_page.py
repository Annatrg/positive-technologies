import allure

from helpers.home_page import HomePageHelper
from helpers.universal import UniversalHelper
from helpers.vacancy_page import VacancyPageHelper

home_page = HomePageHelper()
universal_helper = UniversalHelper()
vacancy_page = VacancyPageHelper()


@allure.title("Переход на страницу с вакансиями")
def test_go_to_vacancy_page():
    with allure.step('Открыть домашнюю страницу'):
        home_page.open_home_page()
    with allure.step('Перейти на страницу списка вакансий'):
        vacancy_page.get_to_vacancy_page()
    with allure.step('Проверить URL страницы'):
        universal_helper.check_url('https://www.ptsecurity.com/ru-ru/about/vacancy/')


@allure.title("Проверка фильтра по направлению вакансии")
def test_profession_filters():
    with allure.step('Открыть страницу с вакансиями'):
        universal_helper.open_page('/about/vacancy/')
    with allure.step('Выбрать фильтр по направлению деятельности'):
        vacancy_page.choose_filter('Информационная безопасность')
    with allure.step('Проверить, что в результатах есть вакансия с указанным направлением'):
        vacancy_page.keyword_appears_in_the_results('Информационная безопасность')
    with allure.step('Проверить, что в результатах нет вакансий с другим направлением'):
        vacancy_page.keyword_missing_from_results('Тестирование')


@allure.title("Проверка открытия страницы с вакансией")
def test_open_vacancy():
    with allure.step('Открыть страницу с вакансиями'):
        universal_helper.open_page('/about/vacancy/')
    with allure.step('Открыть страницу любой вакансии вакансии'):
        vacancy_page.open_vacancy_page('Технический писатель')
    with allure.step('Проверить, что в вакансии присутствуют ключевые слова'):
        vacancy_page.keyword_appears_in_vacancy('Мы ищем технического писателя')
        vacancy_page.keyword_appears_in_vacancy('Что мы ожидаем от кандидатов')
