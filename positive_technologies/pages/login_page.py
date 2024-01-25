from selene import browser, have


class LoginPage:

    def get_to_login_page(self):
        browser.all('.footer-cr__menu fr-menu')
        browser.element('[href="https://partners.ptsecurity.ru/login/#enter"]').click()
        current_url = browser.driver().current_url
        assert "https://partners.ptsecurity.ru/login/#enter" in current_url, \
            f'Текущая ссылка страницы {current_url} не соответствует ожидаемой'


    def type_email(self, value):
        browser.element('#emailCtFace').type(value)
        return self


    def type_password(self, value):
        browser.element('#passAuth').type(value)
        return self


    def check_error_login(self):
        browser.all('.form-final').element_by(have.text('Неверный логин или пароль'))
