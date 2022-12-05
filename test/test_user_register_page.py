import allure
from opencart.tools.generator import generated_user
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
        page.tests_logger.info('test_go_to_user_register_page')
        browser.get(browser.base_url)
        page.user_register.go_to_user_register_page()

        assert browser.title == "Регистрация"
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.title("Checking the presence of main elements on the user register page")
    def test_register_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the user register page """
        page = PageContainer(browser)
        page.tests_logger.info('test_register_page_finds_elements')
        browser.get(browser.base_url)
        page.user_register.go_to_user_register_page()
        page.user_register.checking_presence_elements_user_register_page()

        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.title("Checking valid register a new user on the user register page")
    def test_user_register_valid(self, browser):
        """ Checking valid register a new user on the user register page """
        user = generated_user()
        page = PageContainer(browser)
        page.tests_logger.info('test_user_register_valid')
        browser.get(browser.base_url)
        page.user_register.go_to_user_register_page()
        page.user_register.user_register(user.first_name, user.last_name, user.email,
                                         user.phone, user.password, user.password)

        assert browser.title == "Ваша учетная запись создана!"
        assert "ERROR" not in str(browser.get_log("browser"))