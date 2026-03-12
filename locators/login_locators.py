from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")  # поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")  # поле пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка входа
