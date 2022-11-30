""" Methods of the user register page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.base_page_locators import BasePageLocators
from opencart.tools.generator import generated_user
from opencart.page_objects.locators.user_register_page_locators import UserRegisterPageLocators as rl


class UserRegisterPage(BasePage):
    """ Methods of the user register page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)

    def go_to_user_register_page(self):
        """ Method open user register page of the opencart site """

        with allure.step("Go to user register page"):
            self._click(BasePageLocators.USER_MENU)
            self._click(BasePageLocators.USER_MENU_ITEM_REGISTER)

    def checking_presence_elements_user_register_page(self):
        """ Checking the presence of main elements on the user register page """

        with allure.step("Checking the presence of main elements on the user register page"):
            locators = [rl.CONTENT_TITLE, rl.LOGIN_LINK_IN_FORM, rl.PERSONAL_DETAILS_SECTION, rl.LAST_NAME_FIELD,
                        rl.FIRST_NAME_FIELD, rl.EMAIL_FIELD, rl.PHONE_FIELD, rl.PASSWORD_FIELD, rl.AGREE_CHECKBOX,
                        rl.PASSWORD_CONFIRM_FIELD, rl.CONTINUE_BUTTON]
            for locator in locators:
                self._verify_element_presence(locator)

    def valid_user_register(self):
        """ Register new user on the user register page """
        user = generated_user()
        self._type(rl.FIRST_NAME_FIELD, user.first_name)
        self._type(rl.LAST_NAME_FIELD, user.last_name)
        self._type(rl.EMAIL_FIELD, user.email)
        self._type(rl.PHONE_FIELD, user.phone)
        self._type(rl.PASSWORD_FIELD, user.password)
        self._type(rl.PASSWORD_CONFIRM_FIELD, user.password)
        self._click(rl.AGREE_CHECKBOX)
        self._click(rl.CONTINUE_BUTTON)
