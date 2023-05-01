Feature: order history

  Scenario Outline: 16. user is logged in
    Given web browser is on the home page
    When user clicks on "My Account"
    Then column with <info> is shown
    Examples:
      | info         |
      | My Account   |
      | Order History|
      | Transactions |
      | Downloads    |
      | Logout       |

  Scenario: 17. order history when product is ordered
    Given web browser is on the "Order History" page
    And an item is ordered
    When user clicks on "View"
    Then "Order History" page is shown with ordered product

  Scenario: 18. order history when product is not ordered
    Given web browser is on the "My Account" page
    When user clicks on "View your order history"
    Then "Order History" page is shown with no product
