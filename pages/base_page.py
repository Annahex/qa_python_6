from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    order_button = (By.XPATH, "//div[starts-with(@class,'Header_Nav')]/button[text()='Заказать']")
    main_page_button = (By.XPATH, ".//img[@src='/assets/scooter.svg']/parent::a")
    yandex_button = (By.XPATH, ".//img[@src='/assets/ya.svg']/parent::a")
    order_url = "https://qa-scooter.praktikum-services.ru/order"
    main_url = "https://qa-scooter.praktikum-services.ru/"
    dzen_url = "https://dzen.ru/?yredirect=true"

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки страницы')
    def wait_for_load_base_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_button))

    @allure.step('Проверка открытия страницы заказа')
    def check_order_page_opens(self):
        self.driver.find_element(*self.order_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.order_url))

    @allure.step('Проверка открытия главной страницы')
    def check_main_page_opens(self):
        self.driver.find_element(*self.main_page_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.main_url))

    @allure.step('Проверка открытия страницы Дзена')
    def check_dzen_page_opens(self):
        self.driver.find_element(*self.yandex_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.dzen_url))
