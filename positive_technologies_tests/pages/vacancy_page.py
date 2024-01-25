from selene import browser, be, have


class VacancyPage:

    def get_to_vacancy_page(self):
        browser.all('.nav__item').element_by(have.text('О компании')).click()
        browser.element('[href="/ru-ru/about/vacancy/"]').click()

    def choose_filter(self, filter: str):
        browser.all('.checkbox__label').element_by(have.text(filter)).click()
        browser.element('.button').click()

    def keyword_appears_in_the_results(self, keyword: str):
        browser.all('.listing-wrapper').element_by(have.text(keyword)).should(be.visible)

    def keyword_missing_from_results(self, keyword: str):
        browser.all('.listing-wrapper').element_by(have.text(keyword)).should(be.not_.visible)

    def open_vacancy_page(self, vacancy: str):
        browser.all('.vacancies-list__title').element_by(have.text(vacancy)).click()

    def keyword_appears_in_vacancy(self, keyword: str):
        browser.all('.article__body').element_by(have.text(keyword)).should(be.visible)


vacancy = VacancyPage()
