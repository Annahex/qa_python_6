from ..pages.order_page import OrderPage
import allure


class TestOrderPage:

    @allure.title('Проверка открытия главной страницы')
    def test_open_main_page_from_header(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.wait_for_load_order_page()
        order_page.open_main_page_from_header()
        order_page.check_main_page_opens_from_header()

    @allure.title('Проверка открытия страницы Дзена')
    def test_open_dzen_page_from_header(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.wait_for_load_order_page()
        order_page.open_dzen_page_from_header()
        order_page.check_dzen_page_opens_from_header()

    @allure.title('Проверка создания заказа')
    def test_create_order_from_header(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.wait_for_load_order_page()
        order_page.make_order()
        order_page.check_make_order()
