""" Methods of the catalog page of the opencart site """

import allure
from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.catalog_page_locators import CatalogPageLocators as cl


class CatalogPage(BasePage):
    """ Methods of the catalog page of the opencart site """

    def __init__(self, logger, browser):
        super().__init__(logger, browser)
        self.path = "/index.php?route=product/category&path=20"

    def go_to_catalog_page(self):
        """ Method open catalog page of the opencart site """
        with allure.step("Go to catalog page"):
            self.logger.info("User is on the Catalog Page")
            self.browser.get(self.browser.base_url + self.path)

    def checking_presence_elements_catalog_page(self):
        """ Method checking the presence of main elements on the catalog page """

        with allure.step("Checking the presence of main elements on the catalog page"):
            locators = [cl.MENU_LEFT, cl.LIST_VIEW_BUTTON, cl.GRID_VIEW_BUTTON, cl.PROMO_BANNER,
                        cl.PRODUCT_CARD, cl.PRODUCT_CARD_PRICE, cl.PRODUCT_CARD_IMAGE,
                        cl.PRODUCT_CARD_NAME_LINK, cl.PRODUCT_CARD_ADD_CARD, cl.PRODUCT_CARD_COMPARE,
                        cl.PRODUCT_CARD_ADD_WISHLIST]
            for locator in locators:
                self.is_displayed(locator)