from selenium.webdriver.common.by import By


class MainPageLocators:
    SCOOTER_LOGO = By.XPATH, '//a[contains(@class,"Header_LogoScooter")]'
    YANDEX_LOGO = By.XPATH, '//a[contains(@class,"Header_LogoYandex")]'
    MAIN_PAGE_TITLE = By.XPATH, './/div[contains(@class,"Home_Header") and contains(text(),"Самокат")]'
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.XPATH, './/div[@id="accordion__panel-{}"]/p'
    DZEN_LOGO = By.XPATH, './/a[@aria-label="Логотип Бренда"]'
    DZEN_MAIN_SELECT = By.XPATH, '//li[@aria-selected="true"]//div/span[contains(@class, "navigation-tab__text")]'
