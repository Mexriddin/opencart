""" Element locators by pages"""

from selenium.webdriver.common.by import By


class BasePageLocators:
    _CHOOSE_CURRENCY = (By.ID, "form-currency")
    _CURRENCY_ITEM_EUR = (By.CSS_SELECTOR, "#form-currency button[name='EUR']")
    _CURRENCY_TEM_USD = (By.CSS_SELECTOR, "#form-currency button[name='USD']")
    _CURRENCY_ITEM_RUB = (By.CSS_SELECTOR, "#form-currency button[name='RUB']")
    _CHOOSE_LANGUAGE = (By.ID, "form-language")
    _LANGUAGE_ITEM_RU = (By.CSS_SELECTOR, "#form-language button[name='ru-ru']")
    _LANGUAGE_ITEM_EN = (By.CSS_SELECTOR, "#form-language button[name='en-gb']")
    _PHONE = (By.CLASS_NAME, ".fa-phone")
    _USER_MENU = (By.CLASS_NAME, ".fa-user")
    _USER_MENU_ITEM_REGISTER = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(1)")
    _USER_MENU_ITEM_LOGIN = (By.CSS_SELECTOR, ".dropdown-menu-right > :nth-child(2)")
    _WISH_LIST = (By.ID, "wishlist-total")
    _SHOPPING_CART = (By.CSS_SELECTOR, ".list-inline .fa .fa-shopping-cart")
    _CHECKOUT = (By.CSS_SELECTOR, ".list-inline .fa .fa-share")

    _MENU = (By.CSS_SELECTOR, "#menu")
    _MENU_DESKTOPS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(1)")
    _MENU_DESKTOPS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(1) .see-all")

    _MENU_LAPTOPS_AND_NOTEBOOKS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(2)")
    _MENU_LAPTOPS_AND_NOTEBOOKS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(2) .see-all")

    _MENU_COMPONENTS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(3)")
    _MENU_COMPONENTS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(3) .see-all")

    _MENU_TABLETS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(4)")
    _MENU_SOFTWARE = (By.CSS_SELECTOR, "#menu .nav > :nth-child(5)")
    _MENU_PHONES_AND_PDAS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(6)")
    _MENU_CAMERAS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(7)")

    _MENU_MP3_PLAYERS = (By.CSS_SELECTOR, "#menu .nav > :nth-child(8)")
    _MENU_MP3_PLAYERS_SEE_ALL = (By.CSS_SELECTOR, "#menu .nav > :nth-child(8) .see-all")

    _BREADCRUMB = (By.CSS_SELECTOR, "ul.breadcrumb")
    _FOOTER = (By.CSS_SELECTOR, "footer")

    _CLOSE_SECURITY_ALERT_BUTTON = (By.CSS_SELECTOR, ".close")


class MainPageLocators:
    _SEARCH_FIELD = (By.CSS_SELECTOR, "#serch")
    _CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    _MAIN_SLIDER = (By.CSS_SELECTOR, ".swiper-viewport #slideshow0")
    _FOOTER_SLIDER = (By.CSS_SELECTOR, ".swiper-viewport #carousel0")


class UserAuthPageLocators:
    _CONTENT_TITLE = (By.CSS_SELECTOR, "#content h1")
    _LOGIN_LINK_IN_FORM = (By.CSS_SELECTOR, "#content a[href*='route=account/login']")
    _PERSONAL_DETAILS_SECTION = (By.CSS_SELECTOR, "#account")

    _FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    _LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    _EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    _PHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    _PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    _AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    _CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")


class CatalogPageLocators:
    _CATEGORY_TITLE = (By.CSS_SELECTOR, "#content h2")
    _LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    _GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    _SORT_FIELD = (By.CSS_SELECTOR, "#input-sort")

    _PRODUCT_CARD = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb")
    _PRODUCT_CARD_PRICE = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .price")
    _PRODUCT_CARD_IMAGE = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .image")
    _PRODUCT_CARD_NAME_LINK = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .caption a")
    _PRODUCT_CARD_ADD_CARD = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .fa-shopping-cart")
    _PRODUCT_CARD_ADD_WISHLIST = (By.CSS_SELECTOR,  "#content .row :nth-child(1) .product-thumb .fa-heart")
    _PRODUCT_CARD_COMPARE = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .fa-exchange")
    _PRODUCT_CARD_COMPARE1 = (By.CSS_SELECTOR, "#content .row :nth-child(1) .product-thumb .fa-exchange1")


class ProductPageLocators:
    _PRODUCT_IMAGE = (By.CSS_SELECTOR, ".thumbnails :nth-child(1) a")
    _PRODUCT_IMAGE_CLOSE = (By.CSS_SELECTOR, ".mfp-close")
    _PRODUCT_IMAGE_SLIDE_RIGHT = (By.CSS_SELECTOR, ".mfp-arrow-right")
    _PRODUCT_IMAGE_SLIDE_LEFT = (By.CSS_SELECTOR, ".mfp-arrow-left")

    _DESCRIPTION_TAB = (By.CSS_SELECTOR, ".nav-tabs :nth-child(1) a")
    _DESCRIPTION_CONTENT = (By.CSS_SELECTOR, ".tab-content #tab-description")

    _SPECIFICATION_TAB = (By.CSS_SELECTOR, ".nav-tabs :nth-child(2) a")
    _SPECIFICATION_CONTENT = (By.CSS_SELECTOR, ".tab-content #tab-specification")

    _REVIEWS_TAB = (By.CSS_SELECTOR, ".nav-tabs :nth-child(3) a")
    _REVIEWS_CONTENT = (By.CSS_SELECTOR, ".tab-content #tab-review")

    _PRODUCT_SETTINGS = (By.CSS_SELECTOR, "#content #product")
    _PRODUCT_CART_BUTTON = (By.CSS_SELECTOR, "#product #button-cart")

    _PRODUCT_TITLE = (By.CSS_SELECTOR, "#content h1")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    _PHOTOS = (By.CSS_SELECTOR, "ul.thumbnails")
    _PRODUCT_NAV_BAR = (By.CSS_SELECTOR, "ul.nav-tabs")
    _RATING_BLOCK = (By.CSS_SELECTOR, ".rating")


class SearchPageLocators:
    _SEARCH_INPUT = (By.CSS_SELECTOR, "#input-search")

    _CATEGORY_LIST = (By.CSS_SELECTOR, "[name='category_id']")
    _CATEGORY_DESKTOPS = (By.CSS_SELECTOR, "[name='category_id'] [value='20']")
    _CATEGORY_LAPTOPS_AND_NOTEBOOKS = (By.CSS_SELECTOR, "[name='category_id'] [value='18']")
    _CATEGORY_COMPONENTS = (By.CSS_SELECTOR, "[name='category_id'] [value='25']")
    _CATEGORY_TABLETS = (By.CSS_SELECTOR, "[name='category_id'] [value='57']")
    _CATEGORY_SOFTWARE = (By.CSS_SELECTOR, "[name='category_id'] [value='17']")
    _CATEGORY_PHONES_AND_PDAS = (By.CSS_SELECTOR, "[name='category_id'] [value='24']")
    _CATEGORY_CAMERAS = (By.CSS_SELECTOR, "[name='category_id'] [value='33']")
    _CATEGORY_MP3_PLAYERS = (By.CSS_SELECTOR, "[name='category_id'] [value='34']")

    _SUBCATEGORIES_CHECKBOX = (By.CSS_SELECTOR, "[name=sub_category]")
    _SEARCH_IN_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#description")
    _SEARCH_BUTTON = (By.CSS_SELECTOR, "#content #button-search")

    _VIEW_RESULT_AS_LIST = (By.CSS_SELECTOR, "#list-view")
    _VIEW_RESULT_AS_GRID = (By.CSS_SELECTOR, "#grid-view")
    _PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, "#compare-total")
    _SORT_LIST = (By.CSS_SELECTOR, "#input.log-sort")
    _SET_ITEMS_QUANTITY = (By.CSS_SELECTOR, "#input.log-limit")
    _PRODUCT_CARD = (By.CSS_SELECTOR, ".product-grid")


class AdminAuthPageLocators:
    _LOGO = (By.ID, "header-logo")
    _FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    _USERNAME_FIELD = (By.ID, "input-username")
    _PASSWORD_FIELD = (By.ID, "input-password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    _FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, '.help-block')
    _ERROR_MESSAGE = (By.CSS_SELECTOR, '.alert-dismissible')


class AdminMainPageLocators:
    _CATALOG_MENU_ITEM = (By.ID, "menu-catalog")
    _PRODUCTS_MENU_ITEM = (By.CSS_SELECTOR, "#collapse1 > :nth-child(2)")
    _LOGOUT_BUTTON = (By.CLASS_NAME, 'fa-sign-out')
    _ALERT_DANGER = (By.CLASS_NAME, 'alert-danger')


class AdminProductsPageLocators:
    _COPY_BUTTON = (By.CSS_SELECTOR, ".fa-copy")
    _ADD_NEW_BUTTON = (By.CSS_SELECTOR, ".fa-plus")
    _DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    _SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, "fa-reply")

    _PRODUCT_FORM = (By.CSS_SELECTOR, "#form-product")
    _PRODUCT_FORM_GENERAL = (By.ID, "tab-general")
    _PRODUCT_FORM_DATA = (By.LINK_TEXT, "Data")
    _PRODUCT_FORM_IMAGE = (By.LINK_TEXT, "Image")

    _PRODUCT_FORM_GENERAL_NAME_FIELD = (By.ID, "#input-name1")
    _PRODUCT_FORM_GENERAL_TAG_FIELD = (By.ID, "#input-meta-title1")
    _PRODUCT_FORM_DATA_MODEL_FIELD = (By.ID, "input-model")
    _PRODUCT_FORM_IMAGE_ADD_IMAGE = (By.CSS_SELECTOR, "#tab-image #thumb-image")
    _PRODUCT_FORM_IMAGE_SELECT_IMAGE = (By.CSS_SELECTOR, ".popover .fa-pencil")
    _PRODUCT_FORM_IMAGE_UPLOAD_IMAGE = (By.CSS_SELECTOR, "button .fa-upload")
    _PRODUCT_FORM_IMAGE_REFRESH = (By.CSS_SELECTOR, "#button-refresh.btn")

    _FILTER_BUTTON = (By.ID, "#button-filter")
    _FILTER_INPUT_NAME = (By.ID, "#input-name")
    _FILTER_INPUT_MODEL = (By.ID, "#input-model")
    _FILTER_INPUT_PRICE = (By.ID, "#input-price")
    _FILTER_INPUT_QUANTITY = (By.ID, "input-quantity")
    _FILTER_SELECT_STATUS = (By.ID, "input-status")
    _FILTER_STATUS_ENABLED = (By.CSS_SELECTOR, "#input-status [value='1']")
    _FILTER_STATUS_DISABLED = (By.CSS_SELECTOR, "#input-status [value='0']")

    _SELECT_ALL_PRODUCTS_CHECKBOX = (By.CSS_SELECTOR, ".table thead [type='checkbox']")
    _SORT_BY_NAME = (By.CSS_SELECTOR, "thead tr :nth-child(3)")
    _SORT_BY_MODEL = (By.CSS_SELECTOR, "thead tr :nth-child(4)")
    _SORT_BY_PRICE = (By.CSS_SELECTOR, "thead tr :nth-child(5)")
    _SORT_BY_QUANTITY = (By.CSS_SELECTOR, "thead tr :nth-child(6)")
    _SORT_BY_STATUS = (By.CSS_SELECTOR, "thead tr :nth-child(7)")

    _PRODUCT_ROW_IN_PRODUCTS_TABLE = (By.CSS_SELECTOR, "tbody tr")
    _PRODUCT_ROW_NAME = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
    _PRODUCT_ROW_CHECKBOX = (By.CSS_SELECTOR, "tbody tr:nth-child(1) [type='checkbox']")
    _PRODUCT_ROW_EDIT_BUTTON = (By.CSS_SELECTOR, "tbody tr:nth-child(1) .btn")

    _SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    _FALSE_ALERT = (By.CLASS_NAME, "alert-danger")
    _ERROR_ALERT = (By.CLASS_NAME, 'text-danger')