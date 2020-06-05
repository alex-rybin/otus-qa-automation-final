import pytest

from sources.pages.customer.search_results import StoreSearchPage


@pytest.mark.parametrize('keyword', ['mug', 't-shirt'])
def test_search(browser, keyword):
    page = StoreSearchPage(browser)
    page.search(keyword)

    results = page.product_list.product_cards
    assert results
    assert all(keyword in result.get_description_text().casefold() for result in results)


@pytest.mark.parametrize('keyword, expected_result', [('mug', False), ('123456', True)])
def test_no_results(browser, keyword, expected_result):
    page = StoreSearchPage(browser)
    page.search(keyword)

    assert page.product_list.is_no_results_section_present() is expected_result


@pytest.mark.parametrize('sorting, desc', [('Name, A to Z', False), ('Name, Z to A', True)])
def test_search_name_sorting(browser, sorting, desc):
    page = StoreSearchPage(browser)
    page.search('mug')
    page.sort_dropdown.select(sorting)

    names = [result.get_description_text() for result in page.product_list.product_cards]
    assert names
    assert names == sorted(names, reverse=desc)


@pytest.mark.parametrize(
    'sorting, desc', [('Price, low to high', False), ('Price, high to low', True)]
)
def test_search_price_sorting(browser, sorting, desc):
    page = StoreSearchPage(browser)
    page.search('mug')
    page.sort_dropdown.select(sorting)

    prices = [result.get_price_decimal() for result in page.product_list.product_cards]
    assert prices
    assert prices == sorted(prices, reverse=desc)
