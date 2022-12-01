""" Methods of the admin products page of the opencart site"""
import allure

from opencart.page_objects.pages.base_page import BasePage
from opencart.page_objects.locators.admin_products_page_locators import AdminProductsPageLocators as apl


class AdminProductsPage(BasePage):
    """ Methods of the admin products page of the opencart site"""

    def __init__(self, browser):
        super().__init__(browser)

    def go_to_admin_products_page(self):
        """ Method open admin products page of the opencart site """

        with allure.step("Go to admin products page"):
            self._click(apl.CATALOG_MENU_ITEM, "Catalog menu")
            self._click(apl.PRODUCTS_MENU_ITEM, "Products menu")

    def checking_presence_elements_admin_products_page(self):
        """ Method checking the presence of main elements
        on the admin products page """

        with allure.step("Checking the presence of main elements on the search result page"):
            locators = [apl.ADD_NEW_BUTTON, apl.COPY_BUTTON, apl.DELETE_BUTTON, apl.FILTER_BUTTON,
                        apl.SELECT_ALL_PRODUCTS_CHECKBOX, apl.PRODUCT_ROW_IN_PRODUCTS_TABLE, apl.PRODUCT_ROW_CHECKBOX,
                        apl.PRODUCT_ROW_EDIT_BUTTON]
            for locator in locators:
                self.is_displayed(locator)

    def add_product(self):
        """Method for opening the form for adding a new product
         on the products page of the opencart admin"""
        with allure.step("Opening the form for adding a new product"):
            self._click(apl.ADD_NEW_BUTTON, "Add product button")

    def copy_product(self):
        """ Method for copying 1st product
        on the products page of the opencart admin """
        with allure.step("Copying 1 product from the list"):
            self._click(apl.PRODUCT_ROW_CHECKBOX, "Checkbox product")
            self._click(apl.COPY_BUTTON, "Copy button")

    def edit_product(self):
        """ Method for editing 1st product
        on the products page of the opencart admin """
        with allure.step("Opening the product editing form"):
            self._click(apl.PRODUCT_ROW_EDIT_BUTTON, "Edit product button")

    def delete_product(self):
        """ Method for deleting 1st product
        on the products page of the opencart admin """
        with allure.step("Removing 1st product from the list"):
            self._click(apl.PRODUCT_ROW_CHECKBOX, "Checkbox product")
            self._click(apl.DELETE_BUTTON, "Delete product button")

    def edit_product_name(self, product_name):
        """" Method for editing the product name
        on the products page of the opencart admin """
        with allure.step("Edit product name"):
            self._type(apl.PRODUCT_FORM_GENERAL_NAME_FIELD, product_name, "General:Product name")

    def save_product_form(self):
        """ Method for saving changes in the product form
        on the products page of the opencart admin """
        with allure.step("Saving changes in the product form"):
            self._click(apl.SAVE_BUTTON, "Save button")

    def filter_products_by_name(self, product_name):
        """ Method for filtering products by name
        on the products page of the opencart admin """

        with allure.step("Filtering products by name"):
            self._type(apl.FILTER_INPUT_NAME, product_name, "Filter:Product name")
            self._click(apl.FILTER_BUTTON, "Filter button")

    def clear_filter(self):
        """ Method for clearing filters
        on the products page of the opencart admin """

        with allure.step("Cleaning filters"):
            self._element(apl.FILTER_INPUT_NAME).clear()
            self._click(apl.FILTER_BUTTON, "Filter button")

    def create_new_product(self, product_name, product_tag, product_model):
        """ Creation of a new product """
        with allure.step("Creation of a new product"):
            self.add_product()
            self._type(apl.PRODUCT_FORM_GENERAL_NAME_FIELD, product_name, "General:Product name")
            self._type(apl.PRODUCT_FORM_GENERAL_TAG_FIELD, product_tag, "General:Tag name")
            self._click(apl.PRODUCT_FORM_DATA, "Data form")
            self._type(apl.PRODUCT_FORM_DATA_MODEL_FIELD, product_model, "General:Model name")
            self._click(apl.PRODUCT_FORM_IMAGE, "Image form")
            self._click(apl.PRODUCT_FORM_IMAGE_ADD_IMAGE, "Add image button")
            self._click(apl.PRODUCT_FORM_IMAGE_SELECT_IMAGE, "Select image")
            self._click(apl.PRODUCT_FORM_IMAGE_JPG, "Image")
            self.save_product_form()
