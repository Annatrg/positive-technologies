from selene import browser, be


class HomePage:

    def open_home_page(self):
        browser.open('/')

    def accept_cookies(self):
        browser.element('#onetrust-accept-btn-container').click()
        browser.element('#onetrust-accept-btn-container').should(be.not_.visible)

    def check_banners_is_visible(self):
        browser.element('.cards').should(be.visible)
