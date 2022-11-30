import allure
import pytest

from opencart.tools.page_container import PageContainer
from opencart.page_objects.locators.user_register_page_locators import UserLoginPageLocators, UserRegisterPageLocators


@allure.feature("User Login Page")
class TestUserLoginPage:
    """" Tests of the user login page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking go to the user login page")
    def test_go_to_user_login_page(self, browser):
        """ Checking the go to the user login page """

        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_login.go_to_user_login_page()
        assert browser.title == "Авторизация"

    @allure.title("Checking the presence of main elements on the user login page")
    def test_login_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the user login page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_login.go_to_user_login_page()
        page.user_login.checking_presence_elements_user_login_page()

    @allure.title("Checking valid login a new user on the user login page")
    def test_user_login_valid(self, browser):
        """ Checking valid register a new user on the user login page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_login.go_to_user_login_page()
        page.user_login.login_user(page.user_login.email, page.user_login.password)
        assert browser.title == "Личный Кабинет"

    @allure.title("Checking invalid login a new user on the user login page")
    @pytest.mark.parametrize("email, password", [(page.user_login.email, "1234"),
                                                 ("wrong", page.user_login.password),
                                                 ("", ""),
                                                 ("wrong", "1234")])
    def test_user_login_invalid(self, browser, email, password):
        """ Checking invalid register a new user on the user login page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_login.go_to_user_login_page()
        page.user_login.login_user(email, password)
        assert page.admin_login._verify_element_presence(UserLoginPageLocators.ALERT_DANGER)

    @allure.title("Checking logout from user account")
    def test_logout_from_user_account(self, browser):
        """ Checking logout from user account """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.user_login.go_to_user_login_page()
        page.user_login.login_user(page.user_login.email, page.user_login.password)
        page.user_login.logout_user()
        assert page.admin_login.get_text_element(UserRegisterPageLocators.CONTENT_TITLE) == "Личный кабинет"
