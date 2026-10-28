from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TC_URL = ('https://www.amazon.com/gp/help/customer/display.html/'
          'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get(TC_URL)


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    context.known_windows = set(context.driver.window_handles)


@when('Click on Amazon Privacy Notice link (*see image below)')
def click_privacy_notice_link(context):
    context.driver.find_element(By.LINK_TEXT, 'Privacy Notice').click()
    context.driver.wait.until(EC.new_window_is_opened(list(context.known_windows)))


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    new_window = (set(context.driver.window_handles) - context.known_windows).pop()
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.driver.wait.until(EC.url_contains('privacy'))


@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
