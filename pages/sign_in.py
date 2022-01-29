from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignIn(Page):
    SIGN_IN_BUTTON = (By.ID, 'ap_email')

    def sign_in_page(self):
        self.sign_in(*self.SIGN_IN_BUTTON)


