from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('I am on the login page')
def step_impl(context):
    context.browser = webdriver.Chrome()  # Replace with your desired browser
    context.browser.get('https://www.saucedemo.com/')

@when('I enter {username} as the username')
def step_impl(context,username):
    context.browser.find_element(By.ID,'user-name').send_keys(username)

@when('I enter {password} as the password')
def step_impl(context,password):
    context.browser.find_element(By.ID,'password').send_keys(password)

@when('I click on the login button')
def step_impl(context):
    context.browser.find_element(By.ID,'login-button').click()

@then('I should be redirected to the inventory page')
def step_impl(context):
    time.sleep(5)
    assert 'inventory.html' in context.browser.current_url, 'Not on the inventory page'

def after_all(context):
    context.browser.quit()
