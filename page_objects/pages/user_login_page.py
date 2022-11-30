""" Methods of the user login page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.page_objects.locators.user_register_page_locators import UserLoginPageLocators as ll


class UserLoginPage(BasePage):
    """ Methods of the user login page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)

    email = "test123@gmail.com"
    password = "test123"

    def go_to_user_login_page(self):
        """ Method open user login page of the opencart site """

        with allure.step("Go to user login page"):
            self._click(BasePageLocators.USER_MENU)
            self._click(BasePageLocators.USER_MENU_ITEM_LOGIN)

    def checking_presence_elements_user_login_page(self):
        """ Checking the presence of main elements on the user login page """

        with allure.step("Checking the presence of main elements on the user login page"):
            locators = [ll.CONTENT_TITLE, ll.EMAIL_FIELD, ll.PASSWORD_FIELD, ll.SUBMIT_BUTTON]
            for locator in locators:
                self._verify_element_presence(locator)

    def login_user(self, email, password):
        """ Login user on the user register page """
        self._type(ll.EMAIL_FIELD, email)
        self._type(ll.PASSWORD_FIELD, password)
        self._click(ll.SUBMIT_BUTTON)

    def logout_user(self):
        """ Logout from user account"""
        with allure.step("Logout from user account"):
            self._click(ll.USER_MENU)
            self._click(ll.LOGOUT_BUTTON)