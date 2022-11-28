from selenium.webdriver.common.by import By


class AdminMainPageLocators:
    """ Locators of the admin main page of the opencart site """

    CATALOG_MENU_ITEM = (By.ID, "menu-catalog")
    PRODUCTS_MENU_ITEM = (By.CSS_SELECTOR, "#collapse1 > :nth-child(2)")
    LOGOUT_BUTTON = (By.CLASS_NAME, 'fa-sign-out')
    ALERT_DANGER = (By.CLASS_NAME, 'alert-danger')