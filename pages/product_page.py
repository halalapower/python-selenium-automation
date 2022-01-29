from selenium.webdriver.common.by import By
from pages.base_page import Page



class ProductPage(Page):
    ADD_TO_CART_BTN =
    PRODUCT_NAME =
    PRICE_BUY_BOX =
    COLOR_OPTIONS =
    SELECTED_COLOR =

    def open_product_page(self, product_id):
        self.open_page(f'dp/{product_id}/')

    def get_product_name(self) -> str:
        self.find_element(*self.PRODUCT_NAME).text
        print(f'current product:{product_name}')
        return product_name

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)