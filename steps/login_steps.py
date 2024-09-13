from behave import *
from selenium import webdriver
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage

def before_all(context):
    context.driver = webdriver.Chrome() 
    context.login_page = LoginPage(context.driver)
    context.appointment_page = AppointmentPage(context.driver)

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('I enter {username} as the username')
def step_impl(context,username):
    context.login_page.input_username(username)

@when('I enter {password} as the password')
def step_impl(context,password):
    context.login_page.input_password(password)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('I should be redirected to the Appointment page')
def step_impl(context):
    context.appointment_page.verify_appointment_page_is_opened()

def after_all(context):
    context.driver.quit()
