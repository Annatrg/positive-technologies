from selene import browser, be, have


class UniversalHelper:

    def open_page(self, path: str):
        browser.open(path)

    def check_url(self, url: str):
        browser.should(have.url(url))

    def return_home_page(self):
        browser.element('.header-logo').click()
