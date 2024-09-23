Feature: Make Appointment Functionality for the Health Care Service system

    Scenario: Appointment is created successfully
        Given I am on the login page
        When I login with valid credentials
        And I select Tokyo CURA Healthcare Center as my facility
        And I choose Medicaid as my Healthcare Program
        And I apply for hospital readmission
        And I enter 21/09/2024 as my visit date
        And I enter annual check as my comment
        And I click on the book appointment button
        Then Appointment confirmation is shown