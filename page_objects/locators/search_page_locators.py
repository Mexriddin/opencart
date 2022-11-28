from selenium.webdriver.common.by import By


class SearchPageLocators:
    """ Locators of the search page of the opencart site """

    SEARCH_CONTENT = (By.CSS_SELECTOR, "#content h1")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#input-search")

    CATEGORY_LIST = (By.CSS_SELECTOR, "[name='category_id']")
    CATEGORY_DESKTOPS = (By.CSS_SELECTOR, "[name='category_id'] [value='20']")
    CATEGORY_LAPTOPS_AND_NOTEBOOKS = (By.CSS_SELECTOR, "[name='category_id'] [value='18']")
    CATEGORY_COMPONENTS = (By.CSS_SELECTOR, "[name='category_id'] [value='25']")
    CATEGORY_TABLETS = (By.CSS_SELECTOR, "[name='category_id'] [value='57']")
    CATEGORY_SOFTWARE = (By.CSS_SELECTOR, "[name='category_id'] [value='17']")
    CATEGORY_PHONES_AND_PDAS = (By.CSS_SELECTOR, "[name='category_id'] [value='24']")
    CATEGORY_CAMERAS = (By.CSS_SELECTOR, "[name='category_id'] [value='33']")
    CATEGORY_MP3_PLAYERS = (By.CSS_SELECTOR, "[name='category_id'] [value='34']")

    SUBCATEGORIES_CHECKBOX = (By.CSS_SELECTOR, "[name=sub_category]")
    SEARCH_IN_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#description")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#content #button-search")

    VIEW_RESULT_AS_LIST = (By.CSS_SELECTOR, "#list-view")
    VIEW_RESULT_AS_GRID = (By.CSS_SELECTOR, "#grid-view")
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, "#compare-total")
    SORT_LIST = (By.CSS_SELECTOR, "#input.log-sort")
    SET_ITEMS_QUANTITY = (By.CSS_SELECTOR, "#input.log-limit")
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-grid")
