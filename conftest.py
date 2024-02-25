import allure
import pytest
from selenium import webdriver

import data


@pytest.fixture(scope='function')
@allure.title('Запуск драйвера FireFox')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.get(data.MAIN_PAGE_URL)
    yield driver
    driver.quit()
