from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, '[data-test="results-facets-row"]')

    def verify_search_result(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert product in actual_result, f"Expected to find {product}, got {actual_result}"

    def verify_search_url(self, expected_keyword):
        assert expected_keyword in self.driver.current_url, \
            f"Expected {expected_keyword} not in {self.driver.current_url}"
