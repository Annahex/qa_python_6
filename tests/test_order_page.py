from selenium import webdriver
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
import allure


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.base_page = BasePage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Проверка открытия главной страницы')
    def test_open_main_page_from_header(self):
        self.order_page.open_order_page()
        self.base_page.check_main_page_opens()

    @allure.title('Проверка открытия страницы Дзена')
    def test_open_dzen_page_from_header(self):
        self.order_page.open_order_page()
        self.base_page.wait_for_load_base_page()
        self.base_page.check_dzen_page_opens()

    @allure.title('Проверка создания заказа')
    def test_create_order_from_header(self):
        self.order_page.open_order_page()
        self.base_page.wait_for_load_base_page()
        self.order_page.make_order()
        self.order_page.check_make_order()


