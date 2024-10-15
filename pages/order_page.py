from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:

    order_url = "https://qa-scooter.praktikum-services.ru/order"

    def __init__(self, driver):
        self.driver = driver

    def open_order_page(self):
        self.driver.get(self.order_url)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.order_url))

