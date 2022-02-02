from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *


@given('Open Amazon tc page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                       '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handles
    print(f'Current window handle: {context.original_window}')


@when('click on amazon privacy notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(By.LINK_TEXT, 'Privacy Notice').click()
    context.driver.wait.until(EC.new_window_is_opened)

@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_page_opened(context):
    assert 'https://www.amazon.com/gp/help/customer/' in context.driver.current_url, \
        f'Error, https://www.aboutamazon.com/ not opened'


@then('close new window')
def close_amazon_page(context):
    context.driver.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
