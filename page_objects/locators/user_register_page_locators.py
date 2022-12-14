from selenium.webdriver.common.by import By


class UserRegisterPageLocators:
    """ Locators of the User registration page of the opencart site """

    CONTENT_TITLE = (By.CSS_SELECTOR, "#content h1")
    LOGIN_LINK_IN_FORM = (By.CSS_SELECTOR, "#content a[href*='route=account/login']")
    PERSONAL_DETAILS_SECTION = (By.CSS_SELECTOR, "#account")

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    PHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Продолжить']")


class UserLoginPageLocators:
    """ Locators of the User login page of the opencart site """
    CONTENT_TITLE = (By.CSS_SELECTOR, "#content h2")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Войти']")
    ALERT_DANGER = (By.CLASS_NAME, 'alert-danger')

    USER_MENU = (By.CLASS_NAME, "fa-user")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(5)")