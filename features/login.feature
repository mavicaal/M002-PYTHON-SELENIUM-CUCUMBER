Feature: Login Functionality for the Health Care Service system

    Scenario: Successful Login
        Given I am on the login page
        When I enter John Doe as the username
        And I enter ThisIsNotAPassword as the password
        And I click on the login button
        Then I should be redirected to the Appointment page