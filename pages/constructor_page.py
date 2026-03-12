import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from curl import *


class ConstructorPage(BasePage):

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
        elements = self.find_elements(ConstructorPageLocators.INGREDIENT_DETAILS_LOCATOR)
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
            self.drag_and_drop_with_js(element, target)
        else:
            self.drag_and_drop_standard(element, target)
    
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
    
    @allure.step("Ожидание кнопки оформления заказа")
    def wait_for_order_button(self):
        self.wait_for_element(ConstructorPageLocators.ORDER_BUTTON)

    @allure.step("кликнуть на кнопку оформления заказа")
    def click_order_button(self):
        self.click_on_element(ConstructorPageLocators.ORDER_BUTTON)
 
    @allure.step("Дождаться модального окна с подтверждением заказа")
    def confirm_order(self):
        self.wait_for_element(ConstructorPageLocators.ORDER_MODAL)

    @allure.step("Получить номер заказа в модальном окне подтверждения заказа")
    def get_order_number(self):

        element = self.wait_for_element(ConstructorPageLocators.ORDER_NUMBER_IN_MODAL)
    
        if element.text == "9999":
            self.wait_for_condition(
                lambda driver: driver.find_element(*ConstructorPageLocators.ORDER_NUMBER_IN_MODAL).text != "9999",
                timeout=15
                )
            element = self.driver.find_element(*ConstructorPageLocators.ORDER_NUMBER_IN_MODAL)
    
        return int(element.text)
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        close_buttons = self.find_elements(ConstructorPageLocators.ORDER_MODAL_CLOSE)
        if close_buttons:
            self.js_click(ConstructorPageLocators.ORDER_MODAL_CLOSE)

    @allure.step("Проверить, что пользователь авторизован")
    def is_user_logged_in(self):
        elements = self.find_elements(ConstructorPageLocators.ORDER_BUTTON)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step("Создать заказ и получить его номер")
    def create_order_and_get_number(self):
        self.drag_ingredient_to_basket(ConstructorPageLocators.BUN_FLUORESCENT_LOCATOR)
        self.drag_ingredient_to_basket(ConstructorPageLocators.SPICY_SAUCE_LOCATOR)
        self.click_order_button()
        self.confirm_order()
        order_number = self.get_order_number()
        self.close_order_modal()
        return order_number
