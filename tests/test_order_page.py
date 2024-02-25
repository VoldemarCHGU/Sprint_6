import allure

from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка оформления заказа через верхнюю кнопку')
    def test_order_up_btn_success(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_up_order_button()
        order_page.enter_in_form_order_data()
        status_button_text = order_page.confirm_order_and_get_text_status_button()
        assert "Посмотреть статус" == status_button_text

    @allure.title('Проверка оформления заказа через нижнюю кнопку')
    def test_order_down_btn_success(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_down_order_button()
        order_page.enter_in_form_order_data()
        status_button_text = order_page.confirm_order_and_get_text_status_button()
        assert "Посмотреть статус" == status_button_text
