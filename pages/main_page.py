import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать на вопрос и вернуть текст ответа')
    def question_get_text_after_click(self, item):
        question_locator = self.concat_locator_and_number(MainPageLocators.QUESTION_LOCATOR, item)
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        answer_locator = self.concat_locator_and_number(MainPageLocators.ANSWER_LOCATOR, item)
        return self.get_text_element(answer_locator)

    @allure.step('Нажали на лого "Самокат" (на главной)')
    def click_to_logo_scooter(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Получили текст title на странице')
    def get_text_title(self):
        return self.get_text_element(MainPageLocators.MAIN_PAGE_TITLE)

    @allure.step('Нажать на лого "Яндекс" (на главной)')
    def click_to_logo_yandex(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Поменять вкладку и вернуть её адрес')
    def switch_to_window_and_return_link(self):
        self.switch_to_window(1)
        self.find_element_wait_until(MainPageLocators.DZEN_LOGO)
        active_text = self.find_element_wait_until(MainPageLocators.DZEN_MAIN_SELECT).text
        return self.current_url(), active_text
