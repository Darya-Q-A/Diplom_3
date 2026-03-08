from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.constructor_page_locators import ConstructorPageLocators
from pages.constructor_page import ConstructorPage
from curl import *
import allure
import time


class TestConstructor:

    @allure.title("Тест на переход по клику на «Конструктор»")
    @allure.description("Происходит переход ")
    def test_click_on_button_costructor(self, driver):
        constructor_page = ConstructorPage(driver)
        driver.get(order_feed) #сначала перейдем на ленту заказов, чтобы проверить, что по клику точно переходит на констуктор
        constructor_page.click_on_button_costructor(main_site)
        constructor_page.wait_for_url(main_site)
        assert driver.current_url == main_site, "что-то пошло не так, конструктор отменяется"

    @allure.title("Тест на переход по клику на Ленту заказов")
    @allure.description("Происходит переход ")
    def test_click_on_button_order_feed(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_on_button_order_feed(order_feed)
        assert driver.current_url == order_feed, "что-то пошло не так, лента заказов отменяется"

    @allure.title("Тест на появление всплывающего окно с деталями")
    @allure.description("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    @pytest.mark.parametrize("ingredient_locator, expected_name", ConstructorPageLocators.INGREDIENT_DATA)
    def test_ingredient_modal_window(self, driver, ingredient_locator, expected_name):
        constructor_page = ConstructorPage(driver)
        driver.get(main_site)
    
        constructor_page.click_on_ingredient(ingredient_locator)
        time.sleep(1)  # небольшая пауза для гарантии
    
        assert constructor_page.is_modal_open(), "Окно не открылось"
        modal_text = constructor_page.get_text_in_modal_window()   
        assert expected_name in modal_text

    @allure.title("Тест на закрытие модального окна по клику на крестик")
    @allure.description("Откроем и закроем модальное окно")
    @pytest.mark.parametrize("ingredient_locator", [
        ConstructorPageLocators.BIO_CUTLET_LOCATOR,
        ConstructorPageLocators.CRYSTALS_LOCATOR,
        ConstructorPageLocators.BUN_FLUORESCENT_LOCATOR
        ])
    def test_close_modal_window(self, driver, ingredient_locator):
        constructor_page = ConstructorPage(driver)
        driver.get(main_site)
        constructor_page.click_on_ingredient(ingredient_locator)
        constructor_page.wait_modal_window()
        constructor_page.close_modal_window()

        assert constructor_page.is_close_modal_window(), "Модальное окно с деталями ингредиентов не закрыто" 
   
    @allure.title("При добавлении ингредиента счётчик увеличивается")
    @pytest.mark.parametrize("ingredient_locator, expected_increment", ConstructorPageLocators.INGREDIENT_WITH_INCREMENT)
    def test_increasing_ingredient_counter(self, driver, ingredient_locator, expected_increment):
        constructor_page = ConstructorPage(driver)
        driver.get(main_site)
    
        initial_counter = constructor_page.get_ingredient_counter(ingredient_locator)
        constructor_page.drag_ingredient_to_basket(ingredient_locator)      
        new_counter = constructor_page.get_ingredient_counter(ingredient_locator)
    
        assert new_counter - initial_counter == expected_increment, \
            f"Счётчик увеличился на {new_counter - initial_counter}, ожидалось {expected_increment}"
