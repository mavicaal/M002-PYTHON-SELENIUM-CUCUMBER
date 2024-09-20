from behave import *
from selenium import webdriver
from pages.login_page import LoginPage

def before_scenario(self,context):
    self.driver = webdriver.Chrome() 
    self.login_page = LoginPage(self.driver)

def after_scenario(self,context):
    self.driver.quit()
