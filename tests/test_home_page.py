import allure
from allure_commons.types import Severity

from positive_technologies_tests.pages.home_page import home
from positive_technologies_tests.pages.login_page import login
from positive_technologies_tests.helpers.universal import universal


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
        universal.check_url('https://www.ptsecurity.com/ru-ru/')


def test_failed_login():
    with allure.step('Открыть домашнюю страницу'):
        home.open_home_page()
    with allure.step('Перейти на страницу авторизации для Партнеров'):
        login.get_to_login_page()
    with allure.step('Проверить URL страницы'):
        universal.check_url('https://partners.ptsecurity.ru/login/#enter')
    with allure.step('Ввести адрес электронной почты'):
        login.type_email('test@mail.ru')
    with allure.step('Ввести пароль'):
        login.type_password('password')
    with allure.step('Проверить, что отображается ошибка "Неверный логин или пароль"'):
        login.check_error_login()
