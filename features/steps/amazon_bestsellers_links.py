from behave import *
from selenium.webdriver.common.by import By

TOP_LINKS = (By.CSS_SELECTOR, "#zg_header a")
HEADER = (By.CSS_SELECTOR, "#zg_banner_text")


@given('Open Amazon Bestsellers')
def open_amazon_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')
    context.driver.refresh()


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f'expected {expected_links} but got {actual_links}'


@then("User can click through top links and verify correct page")
def click_thru_top(context):

    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link.text
        link.click()

        header_text = context.driver.find_elements(*HEADER).text

    assert link_text in header_text, f'Expected {link_text} not in {header_text}'
