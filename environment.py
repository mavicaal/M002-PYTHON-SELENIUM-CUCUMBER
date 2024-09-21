import json
from behave import *
from selenium import webdriver
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage

def before_all(context):
    with open("./utils/login.json") as j:
        context.login_data = json.load(j)

def before_scenario(self,context):
    self.driver = webdriver.Chrome() 
    self.login_page = LoginPage(self.driver)
    self.appointment_page = AppointmentPage(self.driver)

def after_scenario(self,context):
    self.driver.quit()
