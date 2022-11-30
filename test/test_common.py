"""Test opencart store """

import allure
from opencart.tools.page_container import PageContainer


@allure.feature('Base Page')
class TestCommon:
    """ Test opencart store"""

    page = PageContainer(browser=None)

    @allure.title("Checking opencart site page opening")
    def test_opencart_main_page_is_open(self, browser):
        """ Checking opencart site page opening """

        page = PageContainer(browser=browser)
        browser.get(browser.base_url)
        homepage_url = browser.current_url
        assert "opencart" in homepage_url
