from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

cancel_order = driver.find_element(By.ID, 'helpsearch')
cancel_order.send_keys('Cancel Order')
cancel_order.send_keys(Keys.ENTER)


actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_text = '"Cancel Items or Orders"'
assert actual_text == expected_text, f"Error! Actual {actual_text} does not match expected {expected_text}"

driver.quit()