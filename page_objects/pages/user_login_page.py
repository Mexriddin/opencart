""" Methods of the user login page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.page_objects.locators.user_register_page_locators import UserLoginPageLocators as ll


class UserLoginPage(BasePage):
    """ Methods of the user login page of the opencart site"""

    def __init__(self, logger, browser):
        super().__init__(logger, browser)

    email = "test123@gmail.com"
    password = "test123"

    def go_to_user_login_page(self):
        """ Method open user login page of the opencart site """

        with allure.step("Go to user login page"):
            self.logger.info("User is on the Login Page")
            self._click(BasePageLocators.USER_MENU, "User menu")
            self._click(BasePageLocators.USER_MENU_ITEM_LOGIN, "Login item")

    def checking_presence_elements_user_login_page(self):
        """ Method checking the presence of main elements on the user login page """

        with allure.step("Checking the presence of main elements on the user login page"):
            locators = [ll.CONTENT_TITLE, ll.EMAIL_FIELD, ll.PASSWORD_FIELD, ll.SUBMIT_BUTTON]
            for locator in locators:
                self.is_displayed(locator)

    def login_user(self, email, password):
        """ Login user on the user register page """
        self._type(ll.EMAIL_FIELD, email, "Email")
        self._type(ll.PASSWORD_FIELD, password, "Password")
        self._click(ll.SUBMIT_BUTTON, "Submit button")

    def logout_user(self):
        """ Logout from user account"""
        with allure.step("Logout from user account"):
            self._click(ll.USER_MENU, "User menu")
            self._click(ll.LOGOUT_BUTTON, "Logout button")