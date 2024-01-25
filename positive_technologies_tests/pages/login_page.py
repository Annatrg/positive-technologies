from selene import browser, have


class LoginPage:

    def get_to_login_page(self):
        browser.all('.footer-cr__menu fr-menu')
        browser.element('[href="https://partners.ptsecurity.ru/login/#enter"]').click()

    def type_email(self, value):
        browser.element('#emailCtFace').type(value)
        return self

    def type_password(self, value):
        browser.element('#passAuth').type(value)
        return self

    def check_error_login(self):
        browser.all('.form-final').element_by(have.text('Неверный логин или пароль'))


login = LoginPage()
