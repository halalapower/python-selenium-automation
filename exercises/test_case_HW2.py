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


######


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
# Amazon logo

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# Continue button
driver.find_element(By.ID, "Continue")
# Need help link
driver.find_element(By.ID, "auth-fpp-link-bottom")
#Other issues with Sign-In link (Search by multiple attributes using 'and')
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and @class='a-link-normal']")
#Create your Amazon account button

driver.find_element(By,ID, "//a [@id= 'createAccountSubmit']" )
###

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome

driver.find_element(By.ID, "nav-search-submit-button")

driver.find_element(By.ID, "nav-search-submit-button")
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//span[@class='icp-nav-flag icp-nav-flag-us']")
driver.find_element(By.XPATH, "//a[@data-csa-c-type='link' and "
                              "@href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

driver.find_element(By.XPATH, "//a [text()='Best Sellers' and @data-csa-c-type='link']")

driver.find_element(By.XPATH, "//div [@id='nav-xshop']/a[text()='Best Sellers'] ")
driver.find_element(By.XPATH, "//a [contains (@href,'/gp/bestsellers/?ref_=nav_cs_bestsellers' ) ]")

