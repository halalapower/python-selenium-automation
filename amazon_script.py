
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Coffee Maker")
driver.find_element(By.ID, 'nav-search-submit-button').click()
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_result = '"coffee Maker"'
assert actual_result == expected_result, f"Error! Actual {actual_result} does not match expected {expected_result}"
driver.quit()

