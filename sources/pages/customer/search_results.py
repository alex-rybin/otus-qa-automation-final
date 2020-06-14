import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sources.components.customer.dropdown_menu import DropdownMenu
from sources.components.customer.product_list import ProductList
from sources.logic.common import Locator
from sources.pages.customer.base import StoreBasePage, StoreBasePageLocators


class StoreSearchPageLocators(StoreBasePageLocators):
    SORT_DROPDOWN = Locator('//div[contains(@class, "products-sort-order")]')
    PRODUCT_LIST = Locator('//div[@id="js-product-list"]')


class StoreSearchPage(StoreBasePage):
    _sort_dropdown = None
    _product_list = None

    @property
    def sort_dropdown(self) -> DropdownMenu:
        if not self._sort_dropdown:
            self._sort_dropdown = DropdownMenu(
                self.browser.find_element(*StoreSearchPageLocators.SORT_DROPDOWN), self.browser
            )
        return self._sort_dropdown

    @property
    def product_list(self) -> ProductList:
        if not self._product_list:
            self._product_list = ProductList(
                self.browser.find_element(*StoreSearchPageLocators.PRODUCT_LIST), self.browser
            )
        return self._product_list

    def search(self, value: str):
        with allure.step(f'Поиск товара {value}'):
            with allure.step(f'Ввод текста {value}'):
                self.search_field.send_keys(value)
            with allure.step(f'Нажатие кнопки Enter'):
                self.search_field.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(StoreSearchPageLocators.PRODUCT_LIST)
        )
