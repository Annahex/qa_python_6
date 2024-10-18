from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from ..urls.urls import MAIN_URL, ORDER_URL, DZEN_URL


class BasePage:
    order_header_button = (By.XPATH, "//div[starts-with(@class,'Header_Nav')]/button[text()='Заказать']")
    main_page_button = (By.XPATH, ".//img[@src='/assets/scooter.svg']/parent::a")
    yandex_button = (By.XPATH, ".//img[@src='/assets/ya.svg']/parent::a")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до нужного элемента')
    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Поиск элемента среди массива по индексу')
    def find_element_by_index(self, locator, index):
        return self.driver.find_elements(*locator)[index]

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание кликабельности элемента')
    def wait_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(tuple(locator)))

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(tuple(locator)))

    @allure.step('Ожидание смены URL')
    def wait_for_url_change(self, url):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(url))

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.driver.get(MAIN_URL)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_load_main_page(self):
        self.wait_for_url_change(MAIN_URL)

    @allure.step('Открытие страницы заказов')
    def open_order_page(self):
        self.driver.get(ORDER_URL)

    @allure.step('Ожидание загрузки страницы заказов')
    def wait_for_load_order_page(self):
        self.wait_for_url_change(ORDER_URL)

    @allure.step('Открытие страницы заказа из шапки')
    def open_order_page_from_header(self):
        self.wait_to_be_clickable(self.order_header_button)
        self.find_element(self.order_header_button).click()

    @allure.step('Проверка открытия страницы заказа из шапки')
    def check_order_page_opens_from_header(self):
        self.wait_for_url_change(ORDER_URL)
        assert self.driver.current_url == ORDER_URL

    @allure.step('Открытие страницы заказа из шапки')
    def open_main_page_from_header(self):
        self.wait_to_be_clickable(self.main_page_button)
        self.find_element(self.main_page_button).click()

    @allure.step('Проверка открытия главной страницы')
    def check_main_page_opens_from_header(self):
        self.wait_for_url_change(MAIN_URL)
        assert self.driver.current_url == MAIN_URL

    @allure.step('Открытие страницы Дзена из шапки')
    def open_dzen_page_from_header(self):
        self.wait_to_be_clickable(self.yandex_button)
        self.find_element(self.yandex_button).click()

    @allure.step('Проверка открытия страницы Дзена')
    def check_dzen_page_opens_from_header(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_url_change(DZEN_URL)
