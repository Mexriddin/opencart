from selenium.webdriver.common.by import By


class MainPageLocators:
    """ Locators of the main page of the opencart site """

    MAIN_SLIDER = (By.CSS_SELECTOR, ".swiper-viewport #slideshow0")
    FOOTER_SLIDER = (By.ID, "carousel0")
    FEATURED_CARD_1 = (By.CSS_SELECTOR, "#content .row > :nth-child(1)")
    FEATURED_CARD_2 = (By.CSS_SELECTOR, "#content .row > :nth-child(2)")
    FEATURED_CARD_3 = (By.CSS_SELECTOR, "#content .row > :nth-child(3)")
    FEATURED_CARD_4 = (By.CSS_SELECTOR, "#content .row > :nth-child(4)")
