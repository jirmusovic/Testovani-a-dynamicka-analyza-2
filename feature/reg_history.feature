Feature: user registration and login

  Scenario: 11. start of a registration of a new user
    Given user is not registered
    And web browser is on the home page
    And user clicks on "My Account" icon
    When user clicks on "Register" icon
    Then page with "Register Account" is shown

  Scenario: 12. registration of a new user
    Given web browser is on the "Register Account" page
    And "Personal Details" is filled
    And "I have read and agree to the Privacy Policy" is checked
    And user is not registered
    When user clicks on "Continue"
    Then page with "Your Account Has Been Created!" is shown

  Scenario: 13. logging in
    Given web browser is on the "Login" page
    And "E-mail Address" is correctly filled out
    And Password is correctly filled out
    When user clicks on "Login"
    Then "My Account" page is shown


