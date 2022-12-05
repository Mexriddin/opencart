""" Methods of the user register page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.page_objects.locators.user_register_page_locators import UserRegisterPageLocators as rl


class UserRegisterPage(BasePage):
    """ Methods of the user register page of the opencart site"""

    def __init__(self, logger, browser):
        super().__init__(logger, browser)

    def go_to_user_register_page(self):
        """ Method open user register page of the opencart site """

        with allure.step("Go to user register page"):
            self.logger.info("User is on the Register Page")
            self._click(BasePageLocators.USER_MENU, "User menu")
            self._click(BasePageLocators.USER_MENU_ITEM_REGISTER, "Register item")

    def checking_presence_elements_user_register_page(self):
        """ Method checking the presence of main elements on the user register page """

        with allure.step("Checking the presence of main elements on the user register page"):
            locators = [rl.CONTENT_TITLE, rl.LOGIN_LINK_IN_FORM, rl.PERSONAL_DETAILS_SECTION, rl.LAST_NAME_FIELD,
                        rl.FIRST_NAME_FIELD, rl.EMAIL_FIELD, rl.PHONE_FIELD, rl.PASSWORD_FIELD, rl.AGREE_CHECKBOX,
                        rl.PASSWORD_CONFIRM_FIELD, rl.CONTINUE_BUTTON]
            for locator in locators:
                self.is_displayed(locator)

    def user_register(self, first_name, last_name, email, phone, password, confirm_password):
        """ Register new user on the user register page """
        self._type(rl.FIRST_NAME_FIELD, first_name, "First name")
        self._type(rl.LAST_NAME_FIELD, last_name, "Last name")
        self._type(rl.EMAIL_FIELD, email, "Email")
        self._type(rl.PHONE_FIELD, phone, "Phone")
        self._type(rl.PASSWORD_FIELD, password, "Password")
        self._type(rl.PASSWORD_CONFIRM_FIELD, confirm_password, "Confirm password")
        self._click(rl.AGREE_CHECKBOX, "Agree checkbox")
        self._click(rl.CONTINUE_BUTTON, "Continue button")
