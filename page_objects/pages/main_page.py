""" Methods of the main page of the opencart site"""

import allure
from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.main_page_locators import MainPageLocators as ml
from opencart.page_objects.locators.base_page_locators import BasePageLocators as bl


class MainPage(BasePage):
    """ Methods of the main page of the opencart site """

    def __init__(self, logger, browser):
        super().__init__(logger, browser)

    def go_to_main_page(self):
        """ Method open main page of the opencart site """

        with allure.step("Go to main page"):
            self.logger.info("User is on the Main Page")
            self.browser.get(self.browser.base_url)

    def checking_presence_elements_main_page(self):
        """ Method checking the presence of main elements on the main page """

        with allure.step("Checking the presence of main elements on the main page"):
            locators = [bl.PHONE, bl.USER_MENU, bl.WISH_LIST, bl.SHOPPING_CART, bl.PHONE,
                        bl.CHECKOUT, bl.LOGO_BUTTON, bl.SEARCH_FIELD, bl.CART_BUTTON,
                        ml.MAIN_SLIDER, ml.FOOTER_SLIDER, ml.FEATURED_CARD_1, ml.FEATURED_CARD_2,
                        ml.FEATURED_CARD_3, ml.FEATURED_CARD_4]
            for locator in locators:
                self.is_displayed(locator)

