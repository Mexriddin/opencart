import allure

from opencart.tools.page_container import PageContainer
from opencart.tools.generator import generated_product
from opencart.page_objects.locators.admin_products_page_locators import AdminProductsPageLocators


@allure.feature("Admin Product Page")
class TestAdminProductPage:
    """" Tests of the admin products page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking go to the admin products page")
    def test_go_to_admin_products_page(self, browser):
        """ Checking the go to the admin products page """

        page = PageContainer(browser)
        page.tests_logger.info('test_go_to_admin_products_page')
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(page.admin_login.login, page.admin_login.password)
        page.admin_products.go_to_admin_products_page()

        assert browser.title == "Товары"
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.title("Checking the presence of main elements on the product page")
    def test_catalog_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the admin products page """
        page = PageContainer(browser)
        page.tests_logger.info('test_catalog_page_finds_elements')
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(page.admin_login.login, page.admin_login.password)
        page.admin_products.go_to_admin_products_page()
        page.admin_products.checking_presence_elements_admin_products_page()

        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.title("Checking add a new product")
    def test_add_new_product(self, browser):
        """ Checking creation of a new product """
        product = generated_product()
        page = PageContainer(browser)
        page.tests_logger.info('test_add_new_product')
        browser.get(browser.base_url)
        page.admin_login.go_to_admin_login_page()
        page.admin_login.login_to_admin(page.admin_login.login, page.admin_login.password)
        page.admin_products.go_to_admin_products_page()
        page.admin_products.create_new_product(product.product_name, product.product_tag, product.product_model)

        assert page.admin_products._element(AdminProductsPageLocators.SUCCESS_ALERT)
        assert "ERROR" not in str(browser.get_log("browser"))