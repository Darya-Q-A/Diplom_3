import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from curl import *

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
        options.headless = True
        
        # путь к Firefox, ибо без этого не работало 
        firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
        if os.path.exists(firefox_path):
            options.binary_location = firefox_path
            
        browser = webdriver.Firefox(options=options)
    
    browser.get(main_site)
    yield browser
    browser.quit()
