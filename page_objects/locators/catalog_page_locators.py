from selenium.webdriver.common.by import By


class CatalogPageLocators:
    """ Locators of the catalog page of the opencart site """
    CATEGORY_TITLE = (By.CSS_SELECTOR, "#content h2")
    MENU_LEFT = (By.CSS_SELECTOR, ".list-group")
    PROMO_BANNER = (By.CSS_SELECTOR, ".swiper-wrapper")
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    SORT_FIELD = (By.CSS_SELECTOR, "#input-sort")

    PRODUCT_CARD = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb")
    PRODUCT_CARD_PRICE = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .price")
    PRODUCT_CARD_IMAGE = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .image")
    PRODUCT_CARD_NAME_LINK = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .caption a")
    PRODUCT_CARD_ADD_CARD = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .fa-shopping-cart")
    PRODUCT_CARD_ADD_WISHLIST = (By.CSS_SELECTOR,  "#content .row :nth-child(1) .product-thumb .fa-heart")
    PRODUCT_CARD_COMPARE = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .fa-exchange")
    PRODUCT_CARD_COMPARE1 = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .fa-exchange1")