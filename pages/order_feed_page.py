import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators



class OrderFeedPage(BasePage):

    @allure.step("Получить значение счётчика выполнено за всё время")
    def get_total_orders_count(self):  
        element = self.wait_for_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получить значение счётчика выполнено за сегодня")
    def get_today_orders_count(self):  
        element = self.wait_for_element(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(element.text)
      
    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDER_NUMBER_IN_PROGRESS)
        return [el.text for el in elements]
    
    @allure.step("Ожидать появления номера заказа в работе")
    def wait_for_order_in_progress(self, order_number, timeout=15):
        self.wait_for_condition(
        lambda driver: str(order_number) in [o.lstrip('0') for o in self.get_orders_in_progress()],
        timeout=timeout
        )

    @allure.step("Проверить, что номер заказа появился в работе")
    def is_order_in_progress(self, order_number):
        orders = self.get_orders_in_progress()
        clean_orders = [order.lstrip('0') for order in orders]    
        return str(order_number) in clean_orders
    
    