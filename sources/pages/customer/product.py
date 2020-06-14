import allure
from selenium.webdriver.remote import webelement

from sources.components.customer.modals.cart_modal import CartModal
from sources.logic.common import Locator
from sources.pages.customer.base import StoreBasePageLocators, StoreBasePage


class StoreProductPageLocators(StoreBasePageLocators):
    TITLE = Locator('//h1[@itemprop="name"]')
    PRICE = Locator('//span[@itemprop="price"]')
    QUANTITY_INPUT = Locator('//input[@id="quantity_wanted"]')
    ADD_TO_CART_BUTTON = Locator('//button[@data-button-action="add-to-cart"]')
    CART_MODAL = Locator('//div[@id="blockcart-modal"]/div/div')


class StoreProductPage(StoreBasePage):
    _title = None
    _price = None
    _quantity_input = None
    _add_to_cart_button = None

    @property
    def title(self) -> str:
        if not self._title:
            self._title = self.browser.find_element(*StoreProductPageLocators.TITLE)
        return self._title.text

    @property
    def price(self) -> str:
        if not self._price:
            self._price = self.browser.find_element(*StoreProductPageLocators.PRICE)
        return self._price.text

    @property
    def quantity_input(self) -> webelement:
        if not self._quantity_input:
            self._quantity_input = self.browser.find_element(
                *StoreProductPageLocators.QUANTITY_INPUT
            )
        return self._quantity_input

    @property
    def add_to_cart_button(self) -> webelement:
        if not self._add_to_cart_button:
            self._add_to_cart_button = self.browser.find_element(
                *StoreProductPageLocators.ADD_TO_CART_BUTTON
            )
        return self._add_to_cart_button

    @property
    def cart_modal(self) -> CartModal:
        return CartModal(
            self.browser.find_element(*StoreProductPageLocators.CART_MODAL), self.browser
        )

    def set_quantity(self, value: int):
        with allure.step(f'Ввод количества товара: {value}'):
            self.quantity_input.clear()
            self.quantity_input.send_keys(value)
