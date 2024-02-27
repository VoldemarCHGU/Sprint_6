import allure
import pytest


class TestOrderPage:
    @allure.title('Проверка оформления заказа через верхнюю кнопку')
    @pytest.mark.parametrize('button', ['down_btn', 'up_btn'])
    def test_order_up_btn_success(self, order_page, button):
        order_page.click_on_order_button(button)
        order_page.enter_in_form_order_data()
        status_button_text = order_page.confirm_order_and_get_text_status_button()
        assert "Посмотреть статус" == status_button_text
