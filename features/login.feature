Feature: Login Functionality for the Health Care Service system

    Scenario: Successful Login
        Given I am on the login page
        When I enter John Doe as the username
        And I enter ThisIsNotAPassword as the password
        And I click on the login button
        Then I should be redirected to the Appointment page

    Scenario: Bad Login
        Given I am on the login page
        When I enter test1 as the username
        And I enter passw1 as the password
        And I click on the login button
        Then Error msg is displayed