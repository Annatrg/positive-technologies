from selene import browser, have, be


def test_banners(open_home_page):
    browser.should(have.url('https://www.ptsecurity.com/ru-ru/'))
    browser.element('.cards').should(be.visible)
