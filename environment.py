from behave import *
from selenium import webdriver
from pages.login_page import LoginPage

def before_scenario(self,context):
    driver = webdriver.Chrome() 
    self.login_page = LoginPage(driver)

# def after_scenario(context):
#     context.driver.quit()
