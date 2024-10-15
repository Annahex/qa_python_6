from selenium import webdriver
from pages.main_page import MainPage
from pages.base_page import BasePage


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.main_page = MainPage(cls.driver)
        cls.base_page = BasePage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_weather_for_selected_settlement(self):
        self.main_page.open_main_page()
        self.main_page.wait_for_load_main_page()
        self.main_page.check_questions_open()

    def test_open_order_page_from_header(self):
        self.main_page.open_main_page()
        self.base_page.wait_for_load_base_page()
        self.base_page.check_order_page_opens()

    def test_order_page_opens_from_body(self):
        self.main_page.open_main_page()
        self.main_page.scroll_to_order_button()
        self.main_page.check_order_page_opens()

