import allure
import pytest
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from curl import *
import time


class TestOrderFeed:
    
    @allure.title("Счётчик выполненных заказов за всё время увеличивается")
    def test_total_orders_counter_increases(self, driver, authorization_user):
        order_feed_page = OrderFeedPage(driver)
        driver.get(order_feed)
        initial_counter = order_feed_page.get_total_orders_count()
        driver.get(main_site)
        constructor_page = ConstructorPage(driver)
        order_number = constructor_page.create_order_and_get_number()
        driver.get(order_feed)
        time.sleep(2)
        final_counter = order_feed_page.get_total_orders_count()
    
        assert final_counter > initial_counter, f'ожидалось увеличение счетчика'

    @allure.title("Счётчик выполненных заказов за сегодня увеличивается")
    @allure.description("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, driver, authorization_user):
        order_feed_page = OrderFeedPage(driver)
        driver.get(order_feed)
        initial_counter = order_feed_page.get_today_orders_count()
        driver.get(main_site)
        constructor_page = ConstructorPage(driver)
        order_number = constructor_page.create_order_and_get_number()
        driver.get(order_feed)
        time.sleep(2)
        final_counter = order_feed_page.get_today_orders_count()

        assert final_counter > initial_counter, f'Счётчик за сегодня не увеличился'   

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    @allure.description("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_in_progress(self, driver, authorization_user, created_order):
        order_feed_page = OrderFeedPage(driver)
        driver.get(order_feed)
        time.sleep(2)
        assert order_feed_page.is_order_in_progress(created_order), f'Номер заказа {created_order} не появился в разделе «В работе»'
            