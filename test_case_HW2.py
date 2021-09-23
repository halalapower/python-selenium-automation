from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

cancel_order = driver.find_element(By.ID, 'helpsearch')
cancel_order.send_keys('Cancel Order')
cancel_order.send_keys(Keys.ENTER)


actual_result = driver.find_element(By.XPATH, "//h1[text() = 'Cancel Items or Orders']").text
expected_result = '"Cancel Items or Orders"'
assert actual_result == expected_result, f"Error! Actual {actual_result} does not match expected {expected_result}"

driver.quit()
