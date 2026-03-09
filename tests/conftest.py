import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data import Credentials
from locators.login_locators import LoginPageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
import os
from curl import *
import time


# фиструра настройки браузера
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--width=1600")
        options.add_argument("--height=900")
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
    else:
        options = Options()
        options.add_argument("--width=1600")
        options.add_argument("--height=900")
        options.headless = False
        
        # путь к Firefox, ибо без этого не работало 
        firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
        if os.path.exists(firefox_path):
            options.binary_location = firefox_path
            
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
    time.sleep(0.5)
    return Credentials.EXISTING_USER

# фиструра создает заказ
@pytest.fixture
def created_order(driver, authorization_user):
    constructor_page = ConstructorPage(driver)
    constructor_page.drag_ingredient_to_basket(ConstructorPageLocators.BUN_FLUORESCENT_LOCATOR)
    constructor_page.drag_ingredient_to_basket(ConstructorPageLocators.SPICY_SAUCE_LOCATOR)
    constructor_page.click_order_button()
    time.sleep(2)
    constructor_page.confirm_order()
    order_number = constructor_page.get_order_number()
    constructor_page.close_order_modal()
    
    return order_number
