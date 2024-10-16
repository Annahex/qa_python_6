from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import allure


class MainPage:

    question_button_1 = [By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']/parent::div"]
    question_button_2 = [By.XPATH, ".//div[text()='Хочу сразу несколько самокатов! Так можно?']/parent::div"]
    question_button_3 = [By.XPATH, ".//div[text()='Как рассчитывается время аренды?']/parent::div"]
    question_button_4 = [By.XPATH, ".//div[text()='Можно ли заказать самокат прямо на сегодня?']/parent::div"]
    question_button_5 = [By.XPATH, ".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']/parent::div"]
    question_button_6 = [By.XPATH, ".//div[text()='Вы привозите зарядку вместе с самокатом?']/parent::div"]
    question_button_7 = [By.XPATH, ".//div[text()='Можно ли отменить заказ?']/parent::div"]
    question_button_8 = [By.XPATH, ".//div[text()='Я жизу за МКАДом, привезёте?']/parent::div"]
    question_title = (By.XPATH, ".//div[text()='Вопросы о важном']")
    order_button = (By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]/button[text()='Заказать']")
    order_url = "https://qa-scooter.praktikum-services.ru/order"
    main_url = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверка открытия вопросов о важном')
    def check_questions_open(self):
        title = self.driver.find_element(*self.question_title)
        self.driver.execute_script("arguments[0].scrollIntoView();", title)
        button_1 = self.driver.find_element(*self.question_button_1)
        button_1.click()
        time.sleep(1)
        assert button_1.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_2 = self.driver.find_element(*self.question_button_2)
        button_2.click()
        time.sleep(1)
        assert button_2.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_3 = self.driver.find_element(*self.question_button_3)
        button_3.click()
        time.sleep(1)
        assert button_3.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_4 = self.driver.find_element(*self.question_button_4)
        button_4.click()
        time.sleep(1)
        assert button_4.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_5 = self.driver.find_element(*self.question_button_5)
        button_5.click()
        time.sleep(1)
        assert button_5.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_6 = self.driver.find_element(*self.question_button_6)
        button_6.click()
        time.sleep(1)
        assert button_6.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_7 = self.driver.find_element(*self.question_button_7)
        button_7.click()
        time.sleep(1)
        assert button_7.find_element(By.XPATH, "following-sibling::*").is_displayed()
        button_8 = self.driver.find_element(*self.question_button_8)
        button_8.click()
        time.sleep(1)
        assert button_8.find_element(By.XPATH, "following-sibling::*").is_displayed()
        time.sleep(1)

    @allure.step('Ожидание загрузки страницы')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.question_title))

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.driver.get(self.main_url)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.main_url))

    @allure.step('Скролл к вопросам о важном')
    def scroll_to_order_button(self):
        title = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", title)

    @allure.step('Проверка открытия страницы заказа')
    def check_order_page_opens(self):
        self.driver.find_element(*self.order_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(self.order_url))

