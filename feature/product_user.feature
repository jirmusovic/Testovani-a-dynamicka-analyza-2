Feature:

        Background:
         Given the administrator is logged in

  Scenario: 9. Viewing a customer list
    Given product was ordered by customer
    When web browser is on the "Customers" page
    Then "Customer List" is shown

  Scenario: 10. editing a customer
    Given product was ordered by customer
    And web browser is on the "Customers" page
    When administrator clicks on "Edit"
    Then administrator can edit customer's profile