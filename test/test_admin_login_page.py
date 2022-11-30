import allure

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

    @allure.title("Checking logged out of your admin account")
    def test_logout_from_admin_account(self, browser):
        """ Checking logged out of your admin account """
        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(page.admin_login.login, page.admin_login.password)
        page.admin_login.logout_from_admin()
