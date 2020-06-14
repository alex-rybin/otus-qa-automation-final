from decimal import Decimal
from typing import List

import allure
from selenium.webdriver.remote import webelement

from sources.components.base import BaseComponent
from sources.logic.common import Locator


class ProductCardLocators:
    FLAGS = Locator('./ul/li')
    DESCRIPTION = Locator('.//h2/a')
    PRICE = Locator('.//span[@class="price"]')
    IMAGE = Locator('.//img')


class ProductCard(BaseComponent):
    _flags = None
    _description = None
    _price = None

    @property
    def flags(self) -> list:
        if not self._flags:
            self._flags = self.element.find_elements(*ProductCardLocators.FLAGS)
        return self._flags

    @property
    def description(self) -> webelement:
        if not self._description:
            self._description = self.element.find_element(*ProductCardLocators.DESCRIPTION)
        return self._description

    @property
    def price(self) -> webelement:
        if not self._price:
            self._price = self.element.find_element(*ProductCardLocators.PRICE)
        return self._price

    def get_flags_text(self) -> List[str]:
        flags = []
        for flag in self.flags:
            flags.append(flag.text)

        return flags

    def get_description_text(self) -> str:
        return self.description.text

    def get_price_text(self) -> str:
        return self.price.text

    def get_price_decimal(self) -> Decimal:
        price = self.price.text.replace('$', '')
        return Decimal(price)

    def click(self):
        with allure.step(f'Клик по товару {self.get_description_text()}'):
            self.element.find_element(*ProductCardLocators.IMAGE).click()
