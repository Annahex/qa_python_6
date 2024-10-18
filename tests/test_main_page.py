from ..pages.main_page import MainPage
import allure
import pytest


class TestMainPage:

    questions = [
        [0, 'Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [1, 'Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [2, 'Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [3, 'Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [4, 'Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [5, 'Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [6, 'Можно ли отменить заказ?', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [7, 'Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'],
    ]

    @allure.title('Проверка открытия вопросов о важном')
    @pytest.mark.parametrize('index, question, answer', questions)
    def test_questions_open(self, driver, index, question, answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_load_main_page()
        main_page.check_question_open(index, question, answer)

    @allure.title('Проверка открытия страницы заказа из шапки')
    def test_open_order_page_from_header(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_load_main_page()
        main_page.open_order_page_from_header()
        main_page.check_order_page_opens_from_header()

    @allure.title('Проверка открытия страницы заказа кнопкой после раздела как это работает')
    def test_order_page_opens_from_body(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_order_button()
        main_page.check_order_page_opens()

