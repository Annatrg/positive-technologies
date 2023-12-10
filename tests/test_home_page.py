from selene import browser, have, be


def test_banners():
    browser.open('')
    browser.should(have.url('https://www.ptsecurity.com/ru-ru/'))
    browser.element('.cards').should(be.visible)


def test_cookies():
    browser.open('')
    browser.element('#onetrust-accept-btn-container').click()
    browser.element('#onetrust-accept-btn-container').should(be.not_.visible)

def test_go_to_home_page():
    browser.open('about/contacts/')
    browser.element('.header-logo').click()
    browser.should(have.url('https://www.ptsecurity.com/ru-ru/'))


