from selenium.webdriver.common.by import By
import allure
from ..urls.urls import ORDER_URL
from .base_page import BasePage


class MainPage(BasePage):

    question_button = [By.XPATH, ".//div[@data-accordion-component='AccordionItemButton']"]
    question_panel = [By.XPATH, ".//div[@data-accordion-component='AccordionItemPanel']"]
    order_button = [By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]/button[text()='Заказать']"]

    @allure.step('Скролл к вопросам о важном')
    def scroll_to_order_button(self):
        button = self.find_element(self.order_button)
        self.scroll_to(button)
        self.wait_for_visibility(self.order_button)

    @allure.step('Проверка открытия вопросов о важном')
    def check_question_open(self, index, question, answer):
        button = self.find_element_by_index(self.question_button, index)
        panel = self.find_element_by_index(self.question_panel, index)
        self.scroll_to(button)
        self.wait_to_be_clickable(self.question_button)
        button.click()
        assert button.text == question
        assert panel.is_displayed()
        assert panel.text == answer

    @allure.step('Проверка открытия страницы заказа')
    def check_order_page_opens(self):
        self.wait_to_be_clickable(self.order_button)
        self.find_element(self.order_button).click()
        self.wait_for_url_change(ORDER_URL)
        assert self.driver.current_url == ORDER_URL


