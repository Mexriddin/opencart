import allure
import pytest

from opencart.tools.page_container import PageContainer


@allure.feature('Main Page')
class TestMainPage:
    """ Tests of the main page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking the presence of main elements on the main page")
    def test_main_page_finds_elements(self, browser):
        """ Checking the presence of main elements on the main page """
        page = PageContainer(browser)
        page.tests_logger.info('test_main_page_finds_elements')
        page.main.go_to_main_page()
        page.main.checking_presence_elements_main_page()

        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.title("Checking switch currency")
    @pytest.mark.parametrize("currency, currency_label", [("EUR", "€"), ("RUB", "руб."), ("USD", "$")])
    def test_switch_currency_from_main_nav(self, browser, currency, currency_label):
        """" Checking switch currency """
        page = PageContainer(browser)
        page.tests_logger.info('test_switch_currency_from_main_nav')
        page.main.go_to_main_page()
        page.main.switch_currency_in_main_nav(to=currency)

        assert page.main.get_currency_text_from_main_nav() == f"{currency_label} Валюта "
        assert "ERROR" not in str(browser.get_log("browser"))

    @allure.title("Checking switch language")
    @pytest.mark.parametrize("language, language_label", [("eng", "Language"), ("ru", "Язык")])
    def test_switch_language_from_main_nav(self, browser, language, language_label):
        """" Checking switch language """
        page = PageContainer(browser)
        page.tests_logger.info('test_switch_language_from_main_nav')
        page.main.go_to_main_page()
        page.main.switch_language_in_main_nav(to=language)

        assert page.main.get_language_text_from_main_nav() == f"{language_label} "
        assert "ERROR" not in str(browser.get_log("browser"))


