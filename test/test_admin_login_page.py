import allure
import pytest

from opencart.tools.page_container import PageContainer
from opencart.page_objects.locators.admin_auth_page_locators import AdminAuthPageLocators


@allure.feature("Admin Login Page")
class TestAdminLoginPage:
    """" Tests of the admin login page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking go to the admin login page")
    def test_go_to_admin_login_page(self, browser):
        """ Checking the go to the admin login page """

        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        assert page.admin_login.get_text_element(AdminAuthPageLocators.FORM_TITLE) == "Введите логин и пароль"

    @allure.title("Checking the presence of main elements on the admin login page")
    def test_login_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the user login page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.checking_presence_elements_admin_login_page()

    @allure.title("Checking valid login an administrator ")
    def test_login_to_admin_valid(self, browser):
        """ Checking valid register a new user on the user login page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(page.admin_login.login, page.admin_login.password)
        assert browser.title == "Панель состояния"

    @allure.title("Checking invalid login an administrator ")
    @pytest.mark.parametrize("login, password", [(page.admin_login.login, "1234"),
                                                 ("wrong", page.admin_login.password),
                                                 ("", ""),
                                                 ("wrong", "1234")])
    def test_login_to_admin_invalid(self, browser, login, password):
        """ Checking invalid register a new user on the user login page """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(login, password)
        assert page.admin_login._verify_element_presence(AdminAuthPageLocators.ALERT_DANGER)

    @allure.title("Checking logout from admin account")
    def test_logout_from_admin_account(self, browser):
        """ Checking logout from admin account """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(page.admin_login.login, page.admin_login.password)
        page.admin_login.logout_from_admin()
        assert page.admin_login.get_text_element(AdminAuthPageLocators.FORM_TITLE) == "Введите логин и пароль"


