from sources.pages.customer.base import StoreBasePage


def test_main_page_loaded(browser):
    page = StoreBasePage(browser)
    assert page.logo


def test_top_menu(browser):
    page = StoreBasePage(browser)
    page.top_menu.click_menu_element('Accessories', 'Home Accessories')
