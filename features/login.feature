Feature: Login Functionality for the Health Care Service system

    Scenario: Successful Login
        Given I am on the login page
        When I login with valid credentials
        Then The Appointment page is shown

    Scenario: Bad Login
        Given I am on the login page
        When I login with invalid credentials
        Then Error msg is displayed