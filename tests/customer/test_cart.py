import allure

from sources.pages.customer.base import StoreBasePage
from sources.pages.customer.catalog import StoreCatalogPage
from sources.pages.customer.product import StoreProductPage


@allure.feature('Корзина')
@allure.title('Кнопка корзины неактивна без товаров')
@allure.severity(allure.severity_level.TRIVIAL)
def test_cart_button_disabled_without_products(browser):
    page = StoreBasePage(browser)
    assert page.is_cart_button_active() is False


@allure.feature('Корзина')
@allure.title('Кнопка корзины активна после добавления товаров')
@allure.severity(allure.severity_level.CRITICAL)
def test_cart_button_enabled_with_products(browser):
    page = StoreCatalogPage(browser)
    page.top_menu.click_menu_element('Accessories', 'Home Accessories')
    page.product_list.product_cards[0].click()

    page = StoreProductPage(browser)
    page.add_to_cart_button.click()
    page.cart_modal.click_continue_shopping()

    assert page.is_cart_button_active()


@allure.feature('Корзина')
@allure.title('Счётчик на кнопке корзины')
@allure.severity(allure.severity_level.NORMAL)
def test_cart_button_counter(browser):
    page = StoreCatalogPage(browser)
    assert page.get_cart_button_count() == 0

    page.top_menu.click_menu_element('Accessories', 'Home Accessories')
    page.product_list.product_cards[0].click()

    page = StoreProductPage(browser)
    page.add_to_cart_button.click()
    page.cart_modal.click_continue_shopping()
    assert page.get_cart_button_count() == 1

    page.set_quantity(2)
    page.add_to_cart_button.click()
    page.cart_modal.click_continue_shopping()
    assert page.get_cart_button_count() == 3
