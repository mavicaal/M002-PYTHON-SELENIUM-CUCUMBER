from behave import *
import time

@given('I am on the login page')
def step_impl(context):
    context.login_page.validate_login_page()
    time.sleep(0.4)

@when('I login with {type} credentials')
def step_impl(context,type):
    username = None
    password = None
    if type == "valid":
        username = context.login_data["success_login"]["username"]
        password = context.login_data["success_login"]["password"]
    elif type == "invalid":
        username = context.login_data["bad_login"]["username"]
        password = context.login_data["bad_login"]["password"]
    else:
        raise ValueError(f"Invalid login type: {type}")
    context.login_page.input_username(username)
    context.login_page.input_password(password)
    context.login_page.click_login_button()
    time.sleep(0.4)

@then('The Appointment page is shown')
def step_impl(context):
    context.login_page.verify_appointment_page_is_opened()
    time.sleep(0.4)

@then('Error msg is displayed')
def step_impl(context):
    context.login_page.verify_error_message()
    time.sleep(0.4)
