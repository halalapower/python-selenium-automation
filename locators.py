

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

