from selenium.webdriver.remote import webdriver


class BasePageLocators:
    pass


class BasePage:
    def __init__(self, browser: webdriver):
        self.browser = browser
