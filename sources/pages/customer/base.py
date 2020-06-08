from selenium.webdriver.remote import webelement

from sources.pages.base import BasePage, BasePageLocators
from sources.logic.common import Locator


class StoreBasePageLocators(BasePageLocators):
    LOGO = Locator('//img[@alt="PrestaShop"]')
    SEARCH_FIELD = Locator('//input[@name="s"]')


class StoreBasePage(BasePage):
    _logo = None
    _search_field = None

    @property
    def logo(self) -> webelement:
        if not self._logo:
            self._logo = self.browser.find_element(*StoreBasePageLocators.LOGO)
        return self._logo

    @property
    def search_field(self) -> webelement:
        if not self._search_field:
            self._search_field = self.browser.find_element(*StoreBasePageLocators.SEARCH_FIELD)
        return self._search_field
