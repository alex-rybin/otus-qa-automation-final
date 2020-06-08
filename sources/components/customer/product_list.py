from typing import List

from sources.components.base import BaseComponent
from sources.components.customer.product_card import ProductCard
from sources.logic.common import Locator


class ProductListLocators:
    TB_CONTAINER = Locator('//div[@class="thumbnail-container"]')
    NO_RESULTS_SECTION = Locator('//section[contains(@class, "page-not-found")]')


class ProductList(BaseComponent):
    _product_cards = None
    _no_results = None

    @property
    def product_cards(self) -> List[ProductCard]:
        if not self._product_cards:
            self._product_cards = [
                ProductCard(card)
                for card in self.element.find_elements(*ProductListLocators.TB_CONTAINER)
            ]
        return self._product_cards

    def is_no_results_section_present(self) -> bool:
        return len(self.element.find_elements(*ProductListLocators.NO_RESULTS_SECTION)) == 1
