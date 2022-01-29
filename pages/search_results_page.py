from selenium.webdriver.common.by import By
from base_page import Page


class SearchResults(Page):
    PRODUCT_PRICE = (By.XPATH, )
    SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def click_first_product(self):
        self.wait_for_element_click(*self.PRODUCT_PRICE)

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)

