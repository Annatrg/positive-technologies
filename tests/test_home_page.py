import allure
from selene import browser

from allure_commons.types import Severity

from positive_technologies.pages.home_page import HomePage
from positive_technologies.helpers.universal import UniversalHelper

home = HomePage()
universal = UniversalHelper()


@allure.title("Проверка наличия баннеров")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
def test_availability_of_banners():
    with allure.step('Открыть домашнюю страницу'):
        home.open_home_page()
    with allure.step('Проверить URL страницы'):
        universal.check_url('https://www.ptsecurity.com/ru-ru/')
    with allure.step('Проверить, что на странице отображаются баннеры'):
        home.check_banners_is_visible()


@allure.title("Принять все cookies")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
def test_accept_cookies():
    with allure.step('Открыть домашнюю страницу'):
        home.open_home_page()
    with allure.step('Принять все куки'):
        home.accept_cookies()


@allure.title("Возвращение на главную страницу через логотип компании")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
def test_go_to_home_page():
    with allure.step('Открыть любую страницу'):
        universal.open_page('/about/contacts/')
    with allure.step('Вернуться на домашнюю страницу через иконку логотипа'):
        universal.return_home_page()
    with allure.step('Проверить URL страницы'):
        current_url = browser.driver().current_url
        assert "https://www.ptsecurity.com/ru-ru/" in current_url, \
            f'Текущая ссылка страницы {current_url} не соответствует ожидаемой'
