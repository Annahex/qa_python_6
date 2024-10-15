from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    order_button = (By.XPATH, "//div[starts-with(@class,'Header_Nav')]/button[text()='Заказать']")
    order_url = "https://qa-scooter.praktikum-services.ru/order"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_base_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_button))

    def check_order_page_opens(self):
        self.driver.find_element(*self.order_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.order_url))
