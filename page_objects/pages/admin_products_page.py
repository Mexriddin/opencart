""" Methods of the admin products page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.page_objects.locators.admin_products_page_locators import AdminProductsPageLocators as apl


class AdminProductsPage(BasePage):
    """ Methods of the admin products page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)

    def go_to_admin_products_page(self):
        """ Method open admin products page of the opencart site """

        with allure.step("Go to admin products page"):
            self._click(apl.CATALOG_MENU_ITEM)
            self._click(apl.PRODUCTS_MENU_ITEM)

    def checking_presence_elements_admin_products_page(self):
        """ Checking the presence of main elements on the admin products page """

        with allure.step("Checking the presence of main elements on the search result page"):
            locators = [apl.ADD_NEW_BUTTON, apl.COPY_BUTTON, apl.DELETE_BUTTON, apl.FILTER_BUTTON,
                        apl.SELECT_ALL_PRODUCTS_CHECKBOX, apl.PRODUCT_ROW_IN_PRODUCTS_TABLE, apl.PRODUCT_ROW_CHECKBOX,
                        apl.PRODUCT_ROW_EDIT_BUTTON]
            for locator in locators:
                self._verify_element_presence(locator)
