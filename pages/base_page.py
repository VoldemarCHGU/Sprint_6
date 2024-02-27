from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def concat_locator_and_number(locator, value):
        method, locator = locator
        return method, locator.format(value)

    def find_element_wait_until(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, data):
        self.find_element_wait_until(locator).send_keys(data)

    def click_element(self, locator):
        self.find_element_wait_until(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element_wait_until(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_element(self, locator):
        return self.find_element_wait_until(locator).text

    def switch_to_window(self, choose_window):
        next_window = self.driver.window_handles[choose_window]
        self.driver.switch_to.window(next_window)
