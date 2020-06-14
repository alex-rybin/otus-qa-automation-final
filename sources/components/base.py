from selenium.webdriver.remote import webelement, webdriver


class BaseComponent:
    def __init__(self, element: webelement, browser: webdriver):
        self.element = element
        self.browser = browser
