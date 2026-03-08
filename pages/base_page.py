import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.constructor_page_locators import ConstructorPageLocators


TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на элемент через JavaScript (обход перекрытий)")
    def js_click(self, locator):
        """Кликает на элемент через JavaScript - игнорирует перекрытия"""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить url страницы")
    @property
    def url(self):
        return self.driver.current_url
    
    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Подождать исчезновения элемента")
    def wait_for_element_close(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Подождать смены url")
    def wait_for_url(self, keyword, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
            lambda driver: keyword in driver.current_url)     

    @allure.step("Скролл до элемента") 
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=TIMEOUT):
        self.wait_for_element(locator, timeout)
        self.driver.find_element(*locator).click()
    
    @allure.step("Получить текст из тега p у элемента")
    def get_text_from_p_element(self, locator):
        self.wait_for_element(locator)
        p_element = self.driver.find_element(*locator).find_element(By.TAG_NAME, 'p')
        return p_element.text
    
    @allure.step("Перетащить из А в Б")
    def drag_ingredient(self, locator_A, locator_B):
        element_A = self.wait_for_element(locator_A)
        element_B = self.wait_for_element(locator_B)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_A, element_B).perform()

    
    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
