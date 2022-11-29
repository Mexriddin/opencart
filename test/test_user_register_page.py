import allure
import pytest

from opencart.tools.page_container import PageContainer


@allure.feature("User Register Page")
class TestUserRegisterPage:
    """" Tests of the user register page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking go to the user register page")
    def test_go_to_user_register_page(self, browser):
        """ Checking the go to the user register page """

        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_register.go_to_user_register_page()
        assert browser.title == "Регистрация"

    @allure.title("Checking the presence of main elements on the user register page")
    def test_register_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the user register page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_register.go_to_user_register_page()
        page.user_register.checking_presence_elements_user_register_page()

    @allure.title("Checking valid register a new user on the user register page")
    def test_user_register_valid(self, browser):
        """ Checking valid register a new user on the user register page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_register.go_to_user_register_page()
        page.user_register.valid_user_register()
        assert browser.title == "Ваша учетная запись создана!"