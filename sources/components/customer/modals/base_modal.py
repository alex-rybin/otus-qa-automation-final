import allure
from selenium.webdriver.remote import webelement, webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sources.components.base import BaseComponent
from sources.logic.common import Locator


class BaseModalLocators:
    HEADER = Locator('.//h4')
    CLOSE_BUTTON = Locator('.//button[@class="close"]')
    MODAL_BACKGROUND = Locator('//div[@class="modal-backdrop fade in"]')


class BaseModal(BaseComponent):
    _header = None
    _close_button = None

    def __init__(self, element: webelement, browser: webdriver):
        super().__init__(element, webelement)
        WebDriverWait(browser, 1).until(EC.visibility_of(element))
        self._background = browser.find_element(*BaseModalLocators.MODAL_BACKGROUND)

    @property
    def header(self) -> str:
        if not self._header:
            self._header = self.element.find_element(*BaseModalLocators.HEADER)
        return self._header.text

    @property
    def close_button(self) -> webelement:
        if not self._close_button:
            self._close_button = self.element.find_element(*BaseModalLocators.CLOSE_BUTTON)
        return self._close_button

    def _wait_until_closed(self):
        WebDriverWait(self.browser, 1).until(
            EC.staleness_of(self._background)
        )

    def close_window(self):
        with allure.step('Клик по кнопке "закрыть" в модальном окне'):
            self.close_button.click()
            self._wait_until_closed()
