from selenium.webdriver.common.by import By


class BasePageLocators:
    """ Locators of the base page of the opencart site """

    CHOOSE_CURRENCY = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
    CURRENCY_ITEM_EUR = (By.CSS_SELECTOR, "#form-currency button[name='EUR']")
    CURRENCY_ITEM_USD = (By.CSS_SELECTOR, "#form-currency button[name='USD']")
    CURRENCY_ITEM_RUB = (By.CSS_SELECTOR, "#form-currency button[name='RUB']")

    CHOOSE_LANGUAGE = (By.CSS_SELECTOR, "#form-language button[data-toggle='dropdown']")
    LANGUAGE_ITEM_RU = (By.CSS_SELECTOR, "#form-language button[name='ru-ru']")
    LANGUAGE_ITEM_EN = (By.CSS_SELECTOR, "#form-language button[name='en-gb']")

    PHONE = (By.CLASS_NAME, "fa-phone")
    USER_MENU = (By.CLASS_NAME, "fa-user")
    USER_MENU_ITEM_REGISTER = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(1)")
    USER_MENU_ITEM_LOGIN = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(2)")
    WISH_LIST = (By.ID, "wishlist-total")
    SHOPPING_CART = (By.CSS_SELECTOR, ".list-inline .fa-shopping-cart")
    CHECKOUT = (By.CSS_SELECTOR, ".list-inline .fa-share")

    LOGO_BUTTON = (By.CSS_SELECTOR, "#logo")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search .btn")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    CART_TOTAL = (By.ID, "cart-total")

    MENU = (By.CSS_SELECTOR, "#menu")
    MENU_DESKTOPS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(1)")
    MENU_DESKTOPS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(1) .see-all")

    MENU_LAPTOPS_AND_NOTEBOOKS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(2)")
    MENU_LAPTOPS_AND_NOTEBOOKS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(2) .see-all")

    MENU_COMPONENTS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(3)")
    MENU_COMPONENTS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(3) .see-all")

    MENU_TABLETS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(4)")
    MENU_SOFTWARE = (By.CSS_SELECTOR, "#menu .nav > :nth-child(5)")
    MENU_PHONES_AND_PDAS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(6)")
    MENU_CAMERAS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(7)")

    MENU_MP3_PLAYERS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(8)")
    MENU_MP3_PLAYERS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(8) .see-all")

    PRODUCT_ITEM = (By.CSS_SELECTOR, "img[title='MacBook']")
    BREADCRUMB = (By.CSS_SELECTOR, "ul.breadcrumb")
    FOOTER = (By.CSS_SELECTOR, "footer")

    CLOSE_SECURITY_ALERT_BUTTON = (By.CSS_SELECTOR, ".close")
