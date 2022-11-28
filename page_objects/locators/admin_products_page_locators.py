from selenium.webdriver.common.by import By


class AdminProductsPageLocators:
    """ Locators of the admin products page of the opencart site """

    COPY_BUTTON = (By.CSS_SELECTOR, ".fa-copy")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, ".fa-plus")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "fa-reply")

    PRODUCT_FORM = (By.CSS_SELECTOR, "#form-product")
    PRODUCT_FORM_GENERAL = (By.ID, "tab-general")
    PRODUCT_FORM_DATA = (By.LINK_TEXT, "Data")
    PRODUCT_FORM_IMAGE = (By.LINK_TEXT, "Image")

    PRODUCT_FORM_GENERAL_NAME_FIELD = (By.ID, "#input-name1")
    PRODUCT_FORM_GENERAL_TAG_FIELD = (By.ID, "#input-meta-title1")
    PRODUCT_FORM_DATA_MODEL_FIELD = (By.ID, "input-model")
    PRODUCT_FORM_IMAGE_ADD_IMAGE = (By.CSS_SELECTOR, "#tab-image #thumb-image")
    PRODUCT_FORM_IMAGE_SELECT_IMAGE = (By.CSS_SELECTOR, ".popover .fa-pencil")
    PRODUCT_FORM_IMAGE_UPLOAD_IMAGE = (By.CSS_SELECTOR, "button .fa-upload")
    PRODUCT_FORM_IMAGE_REFRESH = (By.CSS_SELECTOR, "#button-refresh.btn")

    FILTER_BUTTON = (By.ID, "#button-filter")
    FILTER_INPUT_NAME = (By.ID, "#input-name")
    FILTER_INPUT_MODEL = (By.ID, "#input-model")
    FILTER_INPUT_PRICE = (By.ID, "#input-price")
    FILTER_INPUT_QUANTITY = (By.ID, "input-quantity")
    FILTER_SELECT_STATUS = (By.ID, "input-status")
    FILTER_STATUS_ENABLED = (By.CSS_SELECTOR, "#input-status [value='1']")
    FILTER_STATUS_DISABLED = (By.CSS_SELECTOR, "#input-status [value='0']")

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