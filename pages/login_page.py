import allure
from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators
from curl import login_user


class LoginPage(BasePage):
    
    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(login_user)
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys_to_input(LoginPageLocators.EMAIL_INPUT, email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys_to_input(LoginPageLocators.PASSWORD_INPUT, password)
    
    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.js_click(LoginPageLocators.LOGIN_BUTTON)  # вместо click_on_element
    
    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
