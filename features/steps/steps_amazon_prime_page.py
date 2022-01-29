from behave import given, then
from behave import when
from selenium.webdriver.common.by import By


@given('Open Amazon Prime')
def open_amazon_prime(context):
    context.app.amazon_prime_page.open_amazon_prime()
    

@then('Verify {expected_amount} benefit boxes are present')
def verify_delivery_benefit_boxes_count(context, expected_amount):
    context.app.amazon_prime_page.verify_delivery_benefit_boxes_count(expected_amount)