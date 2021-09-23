
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
#