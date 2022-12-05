""" Class with class instances of all pages """
import logging

from opencart.page_objects.pages.main_page import MainPage
from opencart.page_objects.pages.search_result_page import SearchResultPage
from opencart.page_objects.pages.catalog_page import CatalogPage
from opencart.page_objects.pages.product_page import ProductPage
from opencart.page_objects.pages.user_register_page import UserRegisterPage
from opencart.page_objects.pages.user_login_page import UserLoginPage
from opencart.page_objects.pages.admin_login_page import AdminLoginPage
from opencart.page_objects.pages.admin_products_page import AdminProductsPage


class PageContainer:
    """ Class with class instances of all pages """

    def __init__(self, browser):
        self.logger = logging.getLogger("PAGE NAME")
        self.tests_logger = logging.getLogger("TEST NAME")
        self.main = MainPage(self.logger, browser)
        self.search_result = SearchResultPage(self.logger, browser)
        self.catalog = CatalogPage(self.logger, browser)
        self.product = ProductPage(self.logger, browser)
        self.user_register = UserRegisterPage(self.logger, browser)
        self.user_login = UserLoginPage(self.logger, browser)
        self.admin_login = AdminLoginPage(self.logger, browser)
        self.admin_products = AdminProductsPage(self.logger, browser)