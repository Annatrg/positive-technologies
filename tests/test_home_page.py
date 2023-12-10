import allure
from selene import browser, have, be


@allure.title("Проверка наличия баннеров")
def test_banners():
    browser.open('')
    browser.should(have.url('https://www.ptsecurity.com/ru-ru/'))
    browser.element('.cards').should(be.visible)


@allure.title("Принять все cookies")
def test_cookies():
    browser.open('')
    browser.element('#onetrust-accept-btn-container').click()
    browser.element('#onetrust-accept-btn-container').should(be.not_.visible)


@allure.title("Возвращение на главную страницу")
def test_go_to_home_page():
    browser.open('about/contacts/')
    browser.element('.header-logo').click()
    browser.should(have.url('https://www.ptsecurity.com/ru-ru/'))


