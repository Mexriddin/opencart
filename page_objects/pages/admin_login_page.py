""" Methods of the admin login page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.admin_auth_page_locators import AdminAuthPageLocators as al


class AdminLoginPage(BasePage):
    """ Methods of the admin login page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)
        self.path = "/admin/index.php?route=common/login"

    login = "demo"
    password = "demo"

    def go_to_admin_login_page(self):
        """ Method open admin login page of the opencart site """

        with allure.step("Go to admin login page"):
            self.browser.get(self.browser.base_url + self.path)

    def checking_presence_elements_admin_login_page(self):
        """ Method checking the presence of main elements on the admin login page """

        with allure.step("Checking the presence of main elements on the admin login page"):
            locators = [al.LOGO, al.USERNAME_FIELD, al.PASSWORD_FIELD, al.FORGOTTEN_PASSWORD_LINK, al.LOGIN_BUTTON]
            for locator in locators:
                self.is_displayed(locator)

    def login_to_admin(self, login, password):
        """ Authorization in the admin part of the opencart store """
        with allure.step("Authorization in the admin part of the opencart store"):
            self._type(al.USERNAME_FIELD, login, "Login")
            self._type(al.PASSWORD_FIELD, password, "Password")
            self._click(al.LOGIN_BUTTON, "Login button")

    def logout_from_admin(self):
        """ Logout from admin account"""
        with allure.step("Logout from admin account"):
            self._click(al.LOGOUT_BUTTON, "Logout button")