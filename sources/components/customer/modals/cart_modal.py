from decimal import Decimal

import allure

from sources.components.customer.modals.base_modal import BaseModalLocators, BaseModal
from sources.logic.common import Locator


class CartModalLocators(BaseModalLocators):
    ADDED_PRODUCT_NAME = Locator('.//h6[@class="h6 product-name"]')
    ADDED_PRODUCT_PRICE = Locator('.//p[@class="product-price"]')
    ADDED_PRODUCT_QUANTITY = Locator('.//span[last()]/strong')
    CONTINUE_SHOPPING_BUTTON = Locator('.//button[@class="btn btn-secondary"]')
    PROCEED_TO_CHECKOUT_BUTTON = Locator('.//a[@class="btn btn-primary"]')
    SHIPPING_COST = Locator('.//p[3]/span[@class="value"]')
    TOTAL_PRICE = Locator('.//p[@class="product-total"]/span[@class="value"]')


class CartModal(BaseModal):
    _added_product_name = None
    _added_product_quantity = None
    _added_product_price = None
    _shipping_cost = None
    _total_price = None

    @property
    def added_product_name(self) -> str:
        if not self._added_product_name:
            self._added_product_name = self.element.find_element(
                *CartModalLocators.ADDED_PRODUCT_NAME
            )
        return self._added_product_name.text

    @property
    def added_product_quantity(self) -> int:
        if not self._added_product_quantity:
            self._added_product_quantity = self.element.find_element(
                *CartModalLocators.ADDED_PRODUCT_QUANTITY
            )
        return int(self._added_product_quantity.text)

    @property
    def added_product_price(self) -> str:
        if not self._added_product_price:
            self._added_product_price = self.element.find_element(
                *CartModalLocators.ADDED_PRODUCT_PRICE
            )
        return self._added_product_price.text

    @property
    def total_price(self) -> str:
        if not self._total_price:
            self._total_price = self.element.find_element(*CartModalLocators.TOTAL_PRICE)
        return self._total_price.text

    @property
    def shipping_cost(self) -> str:
        if not self._shipping_cost:
            self._shipping_cost = self.element.find_element(*CartModalLocators.SHIPPING_COST)
        return self._shipping_cost.text

    def get_shipping_cost_decimal(self) -> Decimal:
        value = self.shipping_cost
        if value == 'Free':
            value = 0
        else:
            value = value.replace('$', '')

        return Decimal(value)

    def click_continue_shopping(self):
        with allure.step('Клик по кнопке "Continue Shopping"'):
            self.element.find_element(*CartModalLocators.CONTINUE_SHOPPING_BUTTON).click()

    def click_proceed_to_checkout(self):
        with allure.step('Клик по кнопке "Proceed to Checkout"'):
            self.element.find_element(*CartModalLocators.PROCEED_TO_CHECKOUT_BUTTON).click()
