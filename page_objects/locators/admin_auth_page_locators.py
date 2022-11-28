from selenium.webdriver.common.by import By


class AdminAuthPageLocators:
    """ Locators of the admin page of the opencart site """

    LOGO = (By.ID, "header-logo")
    FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    USERNAME_FIELD = (By.ID, "input-username")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, '.help-block')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.alert-dismissible')