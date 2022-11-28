import allure
import pytest

from opencart.tools.page_container import PageContainer
from opencart.page_objects.locators.product_page_locators import ProductPageLocators


@allure.feature("Product Page")
class TestProductPage:
    """" Tests of the product page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking go to the product page")
    def test_go_to_product_page(self, browser):
        """ Checking the go to the product page """

        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.product.go_to_product_page()
        assert page.search_result.get_text_element(ProductPageLocators.PRODUCT_TITLE) == "MacBook"

    @allure.title("Checking the presence of main elements on the product page")
    def test_catalog_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the product page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.product.go_to_product_page()
        page.product.checking_presence_elements_product_page()