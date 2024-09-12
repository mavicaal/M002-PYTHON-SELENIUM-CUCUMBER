Feature: Login Functionality

    Scenario: Successful Login
        Given I am on the login page
        When I enter standard_user as the username
        And I enter secret_sauce as the password
        And I click on the login button
        Then I should be redirected to the inventory page