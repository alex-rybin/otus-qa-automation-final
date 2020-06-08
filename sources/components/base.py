from selenium.webdriver.remote import webelement


class BaseComponent:
    def __init__(self, element: webelement):
        self.element = element
