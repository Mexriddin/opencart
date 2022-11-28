""" Class with browser property """
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from opencart.page_objects.locators.base_page_locators import BasePageLocators


class BasePage:
    """ Methods of the base page of the opencart site """

    def __init__(self, browser):
        self.browser = browser

    def _verify_element_presence(self, locator):
        """Method waiting for an element to present """
        with allure.step("Wait element presence" + str(locator)):
            try:
                return WebDriverWait(self.browser, self.browser.t).\
                    until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError(f"Cant find element by locator: {locator}")

    def _verify_link_presence(self, link_text):
        """Method waiting for a link to present """
        with allure.step("Waiting for a link to present" + str(link_text)):
            try:
                return WebDriverWait(self.browser, self.browser.t).\
                    until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except TimeoutException:
                raise AssertionError(f"Cant find element by link text: {link_text}")

    def _element(self, locator):
        with allure.step("Element to present" + str(locator)):
            return self._verify_element_presence(locator)

    def _click(self, locator):
        with allure.step("Element to click" + str(locator)):
            element = self._element(locator)
            ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _type(self, locator, value):
        field = self._element(locator).click().clear()
        field.send_keys(value)

    def close_security_alert(self):
        """ Closing warning window on page load """
        self.browser.find_element(BasePageLocators.CLOSE_SECURITY_ALERT_BUTTON).click()

    def get_text_element(self, locator):
        return self._element(locator).text

    def accept_alert(self):
        """ Click OK on the alert """
        alert = self.browser.switch_to.alert
        alert.acept()

    def dismiss_alert(self):
        """ Click Cancel on the alert """
        alert = self.browser.switch_to.alert
        alert.dismiss()

    # Methods of working with MAIN NAV BAR

    @allure.step("Switch currency to: {to}")
    def switch_currency_in_main_nav(self, to):
        if to == "EUR":
            locator = BasePageLocators.CURRENCY_ITEM_EUR
        elif to == "RUB":
            locator = BasePageLocators.CURRENCY_ITEM_RUB
        elif to == "USD":
            locator = BasePageLocators.CURRENCY_ITEM_USD
        else:
            raise RuntimeError("Unsupported currency!")
        self._click(BasePageLocators.CHOOSE_CURRENCY)
        self._click(locator)

    @allure.step("Get currency text")
    def get_currency_text_from_main_nav(self):
        return self._element(BasePageLocators.CHOOSE_CURRENCY).text

    @allure.step("Switch language to: {to}")
    def switch_language_in_main_nav(self, to):
        if to == "eng":
            locator = BasePageLocators.LANGUAGE_ITEM_EN
        elif to == "ru":
            locator = BasePageLocators.LANGUAGE_ITEM_RU
        else:
            raise RuntimeError("Unsupported language!")

        self._click(BasePageLocators.CHOOSE_LANGUAGE)
        self._click(locator)

    @allure.step("Get language title")
    def get_language_text_from_main_nav(self):
        return self._element(BasePageLocators.CHOOSE_LANGUAGE).text
