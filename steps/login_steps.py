from behave import *
import time

@given('I am on the login page')
def step_impl(context):
    context.login_page.validate_login_page()
    time.sleep(0.5)

@when('I enter {username} as the username')
def step_impl(context,username):
    context.login_page.input_username(username)
    time.sleep(0.5)

@when('I enter {password} as the password')
def step_impl(context,password):
    context.login_page.input_password(password)
    time.sleep(0.5)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()
    time.sleep(0.5)

@then('I should be redirected to the Appointment page')
def step_impl(context):
    context.login_page.verify_appointment_page_is_opened()
    time.sleep(0.5)

@then('Error msg is displayed')
def step_impl(context):
    context.login_page.verify_error_message()
    time.sleep(0.5)
