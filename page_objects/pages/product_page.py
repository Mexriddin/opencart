""" Methods of the products page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.page_objects.locators.product_page_locators import ProductPageLocators as pl


class ProductPage(BasePage):
    """ Methods of the products' page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)

    def go_to_product_page(self):
        """ Method open product page of the opencart site """

        with allure.step("Go to product page"):
            self._click(BasePageLocators.PRODUCT_ITEM, "Product item")

    def checking_presence_elements_product_page(self):
        """ Method checking the presence of main elements on the product page """

        with allure.step("Checking the presence of main elements on the search result page"):
            locators = [pl.PRODUCT_IMAGE, pl.DESCRIPTION_TAB, pl.DESCRIPTION_CONTENT, pl.SPECIFICATION_TAB,
                        pl.PRODUCT_SETTINGS, pl.ADD_TO_CART_BUTTON]
            for locator in locators:
                self.is_displayed(locator)
