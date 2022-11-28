""" Class with class instances of all pages """

from opencart.page_objects.pages.main_page import MainPage
from opencart.page_objects.pages.search_result_page import SearchResultPage
from opencart.page_objects.pages.catalog_page import CatalogPage
from opencart.page_objects.pages.product_page import ProductPage


class PageContainer:
    """ Class with class instances of all pages """

    def __init__(self, browser):
        self.main = MainPage(browser)
        self.search_result = SearchResultPage(browser)
        self.catalog = CatalogPage(browser)
        self.product = ProductPage(browser)