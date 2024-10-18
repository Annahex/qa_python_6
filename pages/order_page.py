from selenium.webdriver.common.by import By
from faker import Faker
import re
from datetime import datetime, timedelta
import allure
from .base_page import BasePage


class OrderPage(BasePage):

    first_name_input = [By.XPATH, ".//input[@placeholder='* Имя']"]
    last_name_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    subway_station_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    subway_station_select_element = [By.XPATH, ".//div[text()='Черкизовская']"]
    phone_input = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, ".//button[text()='Далее']"]
    date_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    rental_period_input = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    rental_period_select_element = [By.XPATH, ".//div[text()='сутки']"]
    color_input = [By.XPATH, ".//input[@id='black']"]
    comment_input = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    order_button = (By.XPATH, ".//div[starts-with(@class,'Order_Buttons')]/button[text()='Заказать']")
    confirm_button = [By.XPATH, ".//button[text()='Да']"]
    success_element = [By.XPATH, ".//div[text()='Заказ оформлен']"]

    @allure.step('Создаем заказ')
    def make_order(self):
        tomorrow = datetime.now() + timedelta(days=1)
        fake = Faker("ru_RU")
        self.find_element(self.first_name_input).send_keys(fake.first_name())
        self.find_element(self.last_name_input).send_keys(fake.last_name())
        self.find_element(self.address_input).send_keys(re.sub(r"[^а-яА-Я]", "", fake.address()))
        self.find_element(self.subway_station_input).click()
        self.find_element(self.subway_station_select_element).click()
        self.find_element(self.phone_input).send_keys(re.sub(r"\D", "", fake.phone_number()))
        self.find_element(self.next_button).click()
        self.find_element(self.date_input).send_keys(tomorrow.strftime("%d.%m.%Y"))
        self.find_element(self.rental_period_input).click()
        self.find_element(self.rental_period_select_element).click()
        self.find_element(self.color_input).click()
        self.find_element(self.comment_input).send_keys(fake.text(25))
        self.find_element(self.order_button).click()
        self.wait_to_be_clickable(self.confirm_button)
        self.find_element(self.confirm_button).click()

    @allure.step('Проверяем создание заказа')
    def check_make_order(self):
        self.wait_for_visibility(self.success_element)
        assert self.find_element(self.success_element).is_displayed()








