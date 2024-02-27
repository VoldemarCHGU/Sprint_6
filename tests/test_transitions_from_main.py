import allure


class TestTransitionsFromLogo:
    @allure.title('Переход на главную страницу через лого "Самокат"')
    def test_scooter_button_success(self, main_page):
        main_page.click_to_logo_scooter()
        page_title = main_page.get_text_title()
        assert 'на пару дней' in page_title

    @allure.title('При нажатии на лого "Яндекс" переходим на страницу Дзен')
    def test_go_to_dzen_success(self, main_page):
        main_page.click_to_logo_yandex()
        page_link, active_text = main_page.switch_to_window_and_return_link()
        assert 'dzen.ru' in page_link and active_text == 'Главная'
