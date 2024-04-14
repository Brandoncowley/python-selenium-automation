from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="search"]')
    CART_BTN = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')

    def open_main(self):
        self.open_url("https://www.target.com/")

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(6) # added to wait for ads to clear

    def click_cart(self):
        self.click(*self.CART_BTN)


