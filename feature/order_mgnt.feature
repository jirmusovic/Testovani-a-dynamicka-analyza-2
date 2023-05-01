Feature:  order management

        Background:
          Given the administrator is logged in

  Scenario: 1. new order
    Given web browser is on the "Customers" page
    When order is placed
    Then information about order is shown
    And information about customer is shown

  Scenario: 2. product return
    Given web browser is on the "Product Returns" page
    Then information about return is shown

  Scenario: 4. viewing an order
    Given web browser is on the "Orders" page
    And product is ordered
    When administrator clicks on "View"
    Then order information is shown
