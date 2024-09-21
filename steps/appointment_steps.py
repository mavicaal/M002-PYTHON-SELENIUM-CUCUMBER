from behave import *
import time

@when('I select {facility} as my facility')
def step_impl(context,facility):
    context.appointment_page.select_facility(facility)
    time.sleep(0.4)

@when('I choose {program} as my Healthcare Program')
def step_impl(context,program):
    context.appointment_page.check_health_care_radio_button(program)
    time.sleep(0.4)

@when('I apply for hospital readmission')
def step_impl(context):
    context.appointment_page.check_hospital_readmission()
    time.sleep(0.4)

@when('I enter {date} as my visit date')
def step_impl(context,date):
    context.appointment_page.set_visit_date(date)
    time.sleep(0.4)

@when('I enter {comment} as my comment')
def step_impl(context,comment):
    context.appointment_page.set_comments(comment)
    time.sleep(0.4)

@when('I click on the book appointment button')
def step_impl(context):
    context.appointment_page.click_book_appointment_button()
    time.sleep(0.4)

@then('Appointment confirmation is shown')
def step_impl(context):
    context.appointment_page.verify_appointment_confirmation()
    time.sleep(0.4)