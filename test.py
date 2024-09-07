from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!

print(driver.title)