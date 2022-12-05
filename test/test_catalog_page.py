import allure
import pytest

from opencart.tools.page_container import PageContainer


@allure.feature("Catalog Page")
class TestCatalogPage:
    """" Tests of the catalog page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking the presence of main elements on the catalog page")
    def test_catalog_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the catalog page """
        page = PageContainer(browser)
        page.tests_logger.info('test_catalog_page_finds_elements')
        page.catalog.go_to_catalog_page()
        page.catalog.checking_presence_elements_catalog_page()

        assert "ERROR" not in str(browser.get_log("browser"))
