import allure


from opencart.tools.page_container import PageContainer
from opencart.page_objects.locators.search_page_locators import SearchPageLocators



@allure.feature("Search Result page")
class TestSearchResult:
    """ Tests of the search result page of the opencart site """

    page = PageContainer(browser=None)

    @allure.title("Checking go to the search result page")
    def test_go_to_search_result_page(self, browser):
        """ Checking the go to the search result page """

        page = PageContainer(browser)
        browser.get(browser.base_url)
        page.search_result.go_to_search_result_page()
        assert page.search_result.get_text_element(SearchPageLocators.SEARCH_CONTENT) == "Поиск"

    @allure.title("Checking the presence of main elements on the main page")
    def test_search_result_page_finds_elements(self, browser):
        """Checking the presence of main elements on the search result page"""
        page = PageContainer(browser)
        page.main.go_to_main_page()
        page.search_result.go_to_search_result_page()
        page.search_result.checking_presence_elements_search_result_page()