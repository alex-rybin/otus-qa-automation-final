from selenium.webdriver.remote import webelement

from sources.logic.common import Locator
from sources.pages.customer.base import StoreBasePage, StoreBasePageLocators


class StoreMainPageLocators(StoreBasePageLocators):
    CAROUSEL = Locator('//div[@id="carousel"]')
    FEATURED = Locator('//div[@class="products"]')


class StoreMainPage(StoreBasePage):
    _carousel = None
    _featured = None

    @property
    def carousel(self) -> webelement:
        if not self._carousel:
            self._carousel = self.browser.find_element(*StoreMainPageLocators.CAROUSEL)
        return self._carousel

    @property
    def featured(self) -> webelement:
        if not self._featured:
            self._featured = self.browser.find_element(*StoreMainPageLocators.FEATURED)
        return self._featured
