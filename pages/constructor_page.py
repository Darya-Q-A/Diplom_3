import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from curl import *
import time


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на кнопку конструктор")
    def click_on_button_costructor(self, main_site):
        self.js_click(ConstructorPageLocators.BUTTON_COSTRUCTOR_LOCATOR)
        self.wait_for_url(main_site, timeout=10)

    @allure.step("Кликнуть на кнопку лента заказов")
    def click_on_button_order_feed(self, order_feed):
        self.js_click(ConstructorPageLocators.BUTTON_ORDER_FEED_LOCATOR) 
        self.wait_for_url(order_feed, timeout=10)

    @allure.step("Кликнуть на ингредиент")
    def click_on_ingredient(self, locator):
        self.scroll_to_element(locator)
        self.js_click(locator)

    @allure.step("Ожидание открытия модального окна с деталями")
    def wait_modal_window(self):
        self.wait_for_element(ConstructorPageLocators.INGREDIENT_DETAILS_LOCATOR)
    
    @allure.step("Проверить, открыто ли модальное окно")
    def is_modal_open(self):
        elements = self.driver.find_elements(*ConstructorPageLocators.INGREDIENT_DETAILS_LOCATOR)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step("Ожидание загрузки контейнера с ингредиентами")
    def wait_container_with_ingredients(self):
        self.wait_for_element(ConstructorPageLocators.INGREDIENTS_CONTAINER)

    @allure.step("Получить текст ингредиента в модальном окне")
    def get_text_in_modal_window(self):
        name_element = self.wait_for_element(ConstructorPageLocators.INGREDIENT_NAME_IN_MODAL)
        return name_element.text

    @allure.step("Закрыть модальное окно с деталями")
    def close_modal_window(self):
        self.js_click(ConstructorPageLocators.CROSS_INGREDIENT_DETAILS_LOCATOR)

    @allure.step("Модальное окно с деталями закрыто")
    def is_close_modal_window(self):
        return self.wait_for_element_close(ConstructorPageLocators.INGREDIENT_DETAILS_LOCATOR, timeout=5)

    @allure.step("Перетащить ингредиент в корзину")
    def drag_ingredient_to_basket(self, locator):
        self.scroll_to_element(locator)
        element = self.wait_for_element(locator)
        target = self.wait_for_element(ConstructorPageLocators.BASKET_LOCATOR)
    
        browser_name = self.driver.capabilities.get('browserName', '').lower()
    
        if 'firefox' in browser_name:
            actions = ActionChains(self.driver)
            actions.click_and_hold(element).pause(1).move_to_element(target).pause(1).perform()
    
            # Принудительно вызываем drop через JavaScript
            self.driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('drop', {bubbles: true}));
            arguments[1].dispatchEvent(new MouseEvent('dragend', {bubbles: true}));
            """, target, element)
    
            # Отпускаем кнопку мыши
            actions.release().perform()
            time.sleep(2)
        else:
            # Для Chrome
            actions = ActionChains(self.driver)
            actions.drag_and_drop(element, target).perform()
    
        time.sleep(1)
    
    @allure.step("Проверить наличие счётчика у ингредиента")
    def has_counter(self, locator):
        ingredient = self.wait_for_element(locator)
        elements = ingredient.find_elements(*ConstructorPageLocators.INGREDIENT_COUNTER)
        return len(elements) > 0

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self, locator):
        ingredient = self.wait_for_element(locator)
        counter_element = ingredient.find_element(*ConstructorPageLocators.INGREDIENT_COUNTER)
        return int(counter_element.text)
    
    @allure.step("кликнуть на кнопку оформления заказа")
    def click_order_button(self):
        self.click_on_element(ConstructorPageLocators.ORDER_BUTTON)
 

    @allure.step("Дождаться модального окна с подтверждением заказа")
    def confirm_order(self):
        self.wait_for_element(ConstructorPageLocators.ORDER_MODAL)

    @allure.step("Получить номер заказа в модальном окне подтверждения заказа")
    def get_order_number(self):
        time.sleep(2)
        element = self.wait_for_element(ConstructorPageLocators.ORDER_NUMBER_IN_MODAL, timeout=20)
        return int(element.text)
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        close_buttons = self.driver.find_elements(*ConstructorPageLocators.ORDER_MODAL_CLOSE)
        if close_buttons:
            self.js_click(ConstructorPageLocators.ORDER_MODAL_CLOSE)
        time.sleep(1)

    @allure.step("Проверить, что пользователь авторизован")
    def is_user_logged_in(self):
        elements = self.driver.find_elements(*ConstructorPageLocators.ORDER_BUTTON)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step("Создать заказ и получить его номер")
    def create_order_and_get_number(self):
        self.drag_ingredient_to_basket(ConstructorPageLocators.BUN_FLUORESCENT_LOCATOR)
        self.drag_ingredient_to_basket(ConstructorPageLocators.SPICY_SAUCE_LOCATOR)
        self.click_order_button()
        time.sleep(2)
        self.confirm_order()
        order_number = self.get_order_number()
        self.close_order_modal()
        return order_number
