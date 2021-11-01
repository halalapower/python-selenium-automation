from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'q')
PRODUCT_NAME = (By.ID, 'btnK')


#@given('Open google page')
#def open_google_page(context):
#    context.driver.get('https://www.google.com/')



@when('Click on the first product')
def click_on_first_product(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

@when('Store product name')
def store_product_name(context):
        context.driver.find_element(*SEARCH_SUBMIT).click()
        sleep(1)
@when('Click on Add to cart button')
def click_on_add_to_cart_button(context):
        context.driver.find_element(*SEARCH_SUBMIT).click()
        sleep(1)
@when('Open cart page')
def open_cart_page(context):
        context.driver.find_element(*SEARCH_SUBMIT).click()
        sleep(1)

@then('Verify cart has 1 item(s)')
def verify_cart_has_item(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
@then('Verify cart has correct product')
def verify_cart_has_correct_product(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
