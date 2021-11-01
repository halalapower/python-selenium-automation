
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





@given ('Open Amazon tc page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                       '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
@when ('store original windows')
def store_original_windows(context):
    original_windows = context.driver.current_window_handle

@when ('click on amazon privacy notice link')
def click_on_amazon_privacy_notice_link(context):
    var = context.driver.fin

