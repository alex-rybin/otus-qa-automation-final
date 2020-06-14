from sources.components.customer.dropdown_menu import DropdownMenu
from sources.components.customer.product_list import ProductList
from sources.logic.common import Locator
from sources.pages.customer.base import StoreBasePageLocators, StoreBasePage


class StoreCatalogPageLocators(StoreBasePageLocators):
    CATEGORY_TITLE = Locator('//div[@id="js-product-list-header"]/div/h1')
    CATEGORY_DESCRIPTION = Locator('//div[@id="category-description"]/p/span')
    SORT_DROPDOWN = Locator('//div[contains(@class, "products-sort-order")]')
    PRODUCT_LIST = Locator('//div[@id="js-product-list"]')
    SEARCH_FILTERS = Locator('//div[@id="search_filters"]')


class StoreCatalogPage(StoreBasePage):
    _category_title = None
    _category_description = None
    _sort_dropdown = None
    _product_list = None
    _search_filters = None

    @property
    def category_title(self) -> str:
        if not self._category_title:
            self._category_title = self.browser.find_element(
                *StoreCatalogPageLocators.CATEGORY_TITLE
            )
        return self._category_title.text

    @property
    def category_description(self) -> str:
        if not self._category_description:
            self._category_description = self.browser.find_element(
                *StoreCatalogPageLocators.CATEGORY_DESCRIPTION
            )
        return self._category_description.text

    @property
    def sort_dropdown(self) -> DropdownMenu:
        if not self._sort_dropdown:
            self._sort_dropdown = DropdownMenu(
                self.browser.find_element(*StoreCatalogPageLocators.SORT_DROPDOWN), self.browser,
            )
        return self._sort_dropdown

    @property
    def product_list(self) -> ProductList:
        if not self._product_list:
            self._product_list = ProductList(
                self.browser.find_element(*StoreCatalogPageLocators.PRODUCT_LIST), self.browser,
            )
        return self._product_list
