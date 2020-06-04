from selenium.webdriver.remote import webelement

from sources.pages.base import BasePage, BasePageLocators
from sources.logic.common import Locator


class StoreBasePageLocators(BasePageLocators):
    LOGO = Locator('//img[@alt="PrestaShop"]')


class StoreBasePage(BasePage):
    _logo = None

    @property
    def logo(self) -> webelement:
        if not self._logo:
            self._logo = self.browser.find_element(*StoreBasePageLocators.LOGO)
        return self._logo
