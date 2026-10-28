
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
# Amazon_logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")
# Create_account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# user_name
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_customer_name']")
# email
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_email']")
# password
driver.find_element(By.CSS_SELECTOR, "input.a-input-text a-form-normal a-span12 auth-required-field "
                                     "auth-require-fields-match auth-require-password-validation")
# Re_enter_password
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")

# Create you amazon account
driver.find_element(By.ID, "input#continue")
# condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*= '/gp/help/customer/display.html/ref"
                                     "=ap_register_notification_condition_of_use?']")
# Privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref"
                                     "=ap_register_notification_privacy_notice?']")

# HW Section 2
