import allure

from sources.pages.customer.main import StoreMainPage


@allure.feature('Главная страница')
@allure.title('Наличие основных элементов главной страницы')
@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_loaded(browser):
    page = StoreMainPage(browser)
    elements_visible = [
        page.logo.is_displayed(),
        page.cart_button.is_displayed(),
        page.top_menu.element.is_displayed(),
        page.search_field.is_displayed(),
        page.carousel.is_displayed(),
        page.featured.is_displayed(),
    ]
    expected = [True] * 6
    assert elements_visible == expected
