from sources.pages.customer.base import StoreBasePage


def test_main_page_loaded(browser):
    page = StoreBasePage(browser)
    assert page.logo
