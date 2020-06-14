from selenium.webdriver.remote import webelement

from sources.components.customer.top_menu import TopMenu
from sources.pages.base import BasePage, BasePageLocators
from sources.logic.common import Locator


class StoreBasePageLocators(BasePageLocators):
    LOGO = Locator('//img[@alt="PrestaShop"]')
    SEARCH_FIELD = Locator('//input[@name="s"]')
    TOP_MENU = Locator('//ul[@id="top-menu"]')


class StoreBasePage(BasePage):
    _logo = None
    _search_field = None
    _top_menu = None

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

    @property
    def top_menu(self) -> TopMenu:
        if not self._top_menu:
            self._top_menu = TopMenu(
                self.browser.find_element(*StoreBasePageLocators.TOP_MENU), self.browser
            )
        return self._top_menu
