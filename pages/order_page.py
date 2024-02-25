import random

import allure

import data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Нажимаем на кнопку заказа')
    def click_on_order_button(self, choose_btn):
        if choose_btn == "down_btn":
            button = OrderPageLocators.DOWN_BUTTON
        else:
            button = OrderPageLocators.UP_BUTTON
        self.scroll_to_element(button)
        self.click_element(button)

    @allure.step('Вводим имя')
    def input_send_name(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Вводим фамилию')
    def input_send_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Вводим адрес')
    def input_send_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбираем метро')
    def input_send_metro(self, metro):
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.find_element_wait_until(OrderPageLocators.METRO_INPUT).send_keys(metro)
        metro_station = self.concat_locator_and_number(OrderPageLocators.METRO_STATION, metro)
        self.click_element(metro_station)

    @allure.step('Заполнить телефон')
    def input_send_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Заполнить поле даты заказа (Дата: {date})')
    def input_send_date(self, date):
        self.send_keys(OrderPageLocators.DATA_INPUT, date)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбираем cрок аренды')
    def input_send_rental_time(self):
        self.click_element(OrderPageLocators.DROP_MENU_TIME_ARROW)
        random_rental_time = random.choice(data.RENTAL_TIME)
        locator_rental_time = self.concat_locator_and_number(OrderPageLocators.DROP_MENU_RENTAL_TIME,
                                                             random_rental_time)
        self.click_element(locator_rental_time)

    @allure.step('Подтверждение заказа')
    def confirm_order_and_get_text_status_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ACCEPT_BUTTON)
        return self.get_text_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step('Вводим данные пользователя для заказа')
    def enter_in_form_order_data(self):
        self.input_send_name(data.TEST_USER_NAME)
        self.input_send_surname(data.TEST_USER_SURNAME)
        self.input_send_address(data.TEST_USER_ADDRESS)
        self.input_send_metro(data.TEST_USER_METRO)
        self.input_send_phone(data.TEST_USER_PHONE)
        self.click_on_next_button()
        self.input_send_date(data.TEST_DATA)
        self.input_send_rental_time()
