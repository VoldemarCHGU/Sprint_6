import allure
import pytest
from selenium import webdriver

import data
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
@allure.title('Запуск драйвера FireFox')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(data.MAIN_PAGE_URL)
    return MainPage(driver)


@pytest.fixture(scope='function')
def order_page(driver):
    driver.get(data.MAIN_PAGE_URL)
    return OrderPage(driver)
