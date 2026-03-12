import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options
from data import Credentials
from locators.login_locators import LoginPageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
import os
from curl import *


# фиструра настройки браузера
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--width=1600")
        options.add_argument("--height=900")
        options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    else:
        options = Options()
        options.add_argument("--width=1600")
        options.add_argument("--height=900")
        options.headless = True
      
        browser = webdriver.Firefox(options=options)
    
    browser.get(main_site)
    yield browser
    browser.quit()

# фиструра авторизации пользователя (т.к. только авторизованный пользователь может сделать заказ)
@pytest.fixture
def authorization_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(Credentials.EXISTING_USER["email_user"], Credentials.EXISTING_USER["password_user"])
    constructor_page = ConstructorPage(driver)
    constructor_page.wait_for_order_button()
    return Credentials.EXISTING_USER

# фиструра создает заказ
@pytest.fixture
def created_order(driver, authorization_user):
    constructor_page = ConstructorPage(driver)
    constructor_page.drag_ingredient_to_basket(ConstructorPageLocators.BUN_FLUORESCENT_LOCATOR)
    constructor_page.drag_ingredient_to_basket(ConstructorPageLocators.SPICY_SAUCE_LOCATOR)
    constructor_page.click_order_button()
    constructor_page.confirm_order()
    order_number = constructor_page.get_order_number()
    constructor_page.close_order_modal()
    
    return order_number
