import allure

from opencart.tools.page_container import PageContainer


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