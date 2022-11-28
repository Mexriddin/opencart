""" Methods of the search result page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.page_objects.locators.search_page_locators import SearchPageLocators as sl


class SearchResultPage(BasePage):
    """ Methods of the search result page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)

    def go_to_search_result_page(self):
        """ Method open search result page of the opencart site """

        with allure.step("Go to search result page"):
            self._click(BasePageLocators.SEARCH_BUTTON)

    def checking_presence_elements_search_result_page(self):
        """ Checking the presence of main elements on the search result page """

        with allure.step("Checking the presence of main elements on the search result page"):
            locators = [sl.SEARCH_INPUT, sl.CATEGORY_LIST, sl.CATEGORY_DESKTOPS,
                        sl.CATEGORY_LAPTOPS_AND_NOTEBOOKS, sl.CATEGORY_COMPONENTS, sl.CATEGORY_TABLETS,
                        sl.CATEGORY_SOFTWARE, sl.CATEGORY_PHONES_AND_PDAS, sl.CATEGORY_CAMERAS,
                        sl.CATEGORY_MP3_PLAYERS, sl.SUBCATEGORIES_CHECKBOX, sl.SEARCH_BUTTON,
                        sl.SEARCH_IN_PRODUCT_DESCRIPTION]
            for locator in locators:
                self._verify_element_presence(locator)
