from decimal import Decimal

import allure

from sources.pages.customer.catalog import StoreCatalogPage
from sources.pages.customer.product import StoreProductPage


@allure.feature('Корзина')
@allure.title('Имя добавленного в корзину товара')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_product_name(browser):
    page = StoreCatalogPage(browser)
    page.top_menu.click_menu_element('Accessories', 'Home Accessories')
    page.product_list.product_cards[0].click()

    page = StoreProductPage(browser)
    product_name = page.title
    page.add_to_cart_button.click()

    assert page.cart_modal.added_product_name.casefold() == product_name.casefold()


@allure.feature('Корзина')
@allure.title('Количество добавленного в корзину товара')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_quantity(browser):
    quantity = 3

    page = StoreCatalogPage(browser)
    page.top_menu.click_menu_element('Accessories', 'Stationery')
    page.product_list.product_cards[0].click()

    page = StoreProductPage(browser)
    page.set_quantity(quantity)
    page.add_to_cart_button.click()

    assert page.cart_modal.added_product_quantity == quantity


@allure.feature('Корзина')
@allure.title('Стоимость заказа при добавлении нескольких экземпляров товара')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_total_price(browser):
    quantity = 3

    page = StoreCatalogPage(browser)
    page.top_menu.click_menu_element('Art')
    page.product_list.product_cards[0].click()

    page = StoreProductPage(browser)
    price = page.price
    page.set_quantity(quantity)
    page.add_to_cart_button.click()

    expected_price = (
        round(Decimal(price.replace("$", "")) * quantity, 2)
        + page.cart_modal.get_shipping_cost_decimal()
    )

    assert page.cart_modal.total_price == f'${expected_price}'
