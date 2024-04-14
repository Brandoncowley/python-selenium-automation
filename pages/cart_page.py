from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):

    EMPTY_CART_TXT = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def verify_empty_cart(self):
        actual_result = self.find_element(*self.EMPTY_CART_TXT)
        assert actual_result, f'Empty cart text not found'

