from selenium.webdriver.common.by import By


class ProductPageLocators:
    """ Locators of the product page of the opencart site """

    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".thumbnails :nth-child(1) a")
    PRODUCT_IMAGE_CLOSE = (By.CSS_SELECTOR, ".mfp-close")
    PRODUCT_IMAGE_SLIDE_RIGHT = (By.CSS_SELECTOR, ".mfp-arrow-right")
    PRODUCT_IMAGE_SLIDE_LEFT = (By.CSS_SELECTOR, ".mfp-arrow-left")

    DESCRIPTION_TAB = (By.CSS_SELECTOR, ".nav-tabs :nth-child(1) a")
    DESCRIPTION_CONTENT = (By.CSS_SELECTOR, ".tab-content #tab-description")

    SPECIFICATION_TAB = (By.CSS_SELECTOR, ".nav-tabs :nth-child(2) a")
    SPECIFICATION_CONTENT = (By.CSS_SELECTOR, ".tab-content #tab-specification")

    REVIEWS_TAB = (By.CSS_SELECTOR, ".nav-tabs :nth-child(3) a")
    REVIEWS_CONTENT = (By.CSS_SELECTOR, ".tab-content #tab-review")

    PRODUCT_SETTINGS = (By.CSS_SELECTOR, "#content #product")
    PRODUCT_CART_BUTTON = (By.CSS_SELECTOR, "#product #button-cart")

    PRODUCT_TITLE = (By.CSS_SELECTOR, "#content h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    PHOTOS = (By.CSS_SELECTOR, "ul.thumbnails")
    PRODUCT_NAV_BAR = (By.CSS_SELECTOR, "ul.nav-tabs")
    RATING_BLOCK = (By.CSS_SELECTOR, ".rating")