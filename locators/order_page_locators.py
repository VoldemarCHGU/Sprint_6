from selenium.webdriver.common.by import By


class OrderPageLocators:
    UP_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g'  #
    DOWN_BUTTON = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button'

    NAME_INPUT = By.XPATH, './/div[text()="Введите корректное имя"]/parent::div/input'
    SURNAME_INPUT = By.XPATH, './/div[text()="Введите корректную фамилию"]/parent::div/input'
    ADDRESS_INPUT = By.XPATH, './/div[text()="Введите корректный адрес"]/parent::div/input'
    METRO_INPUT = By.XPATH, './/div[@class="select-search__value"]/input'
    METRO_STATION = By.XPATH, './/li[@class="select-search__row"]/button/div[contains(text(),"{}")]'
    PHONE_INPUT = By.XPATH, './/div[text()="Введите корректный номер"]/parent::div/input'

    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'

    DATA_INPUT = By.XPATH, './/div[@class="react-datepicker__input-container"]/input'

    DROP_MENU_TIME_ARROW = By.XPATH, './/span[@class="Dropdown-arrow"]'
    DROP_MENU_RENTAL_TIME = By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="{}"]'

    ORDER_BUTTON = By.XPATH, './/button[contains(@class,"Button_Middle") and text()="Заказать"]'
    ACCEPT_BUTTON = By.XPATH, './/button[text()="Да"]'
    STATUS_BUTTON = By.XPATH, './/div[@class="Order_NextButton__1_rCA"]/button'
