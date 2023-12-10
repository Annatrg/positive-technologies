from selene import browser, have, be

def test_go_to_vacancy_page():
    browser.open('')
    browser.all('.nav__item').element_by(have.text('О компании')).click()
    browser.element('[href="/ru-ru/about/vacancy/"]').click()
    browser.should(have.url('https://www.ptsecurity.com/ru-ru/about/vacancy/'))


def test_profession_filters():
    browser.open('about/vacancy')
    browser.all('.checkbox__label').element_by(have.text('Информационная безопасность')).click()
    browser.element('.button').click()
    browser.all('.listing-wrapper').element_by(have.text('Информационная безопасность')).should(be.visible)
    browser.all('.listing-wrapper').element_by(have.text('Тестирование')).should(be.not_.visible)


def test_test():
    browser.open('about/vacancy')
   # browser.all('.vacancies-list__title').element_by(have.text('Технический писатель')).locate().click()
    browser.all('.vacancies-list__title').element_by(have.text('Технический писатель')).click()
    browser.all('.article__body').element_by(have.text('Мы ищем технического писателя')).should(be.visible)
    browser.all('.article__body').element_by(have.text('Что мы ожидаем от кандидатов:')).should(be.visible)
