Feature: user and product management

          Background:
            Given the administrator is logged in


  Scenario: 6. start of adding a new product
    Given web browser is on the "Products" page
    When administrator clicks on "Add new"
    Then "Add Product" page is shown

  Scenario: 7. adding a new product
    Given web browser is on the "Add Product" page
    And all of the information is filled out
    When administrator clicks on "Save"
    Then product is modified

  Scenario: 8. viewing a product category
    Given web browser is on the home page
    When administrator clicks on "Categories"
    Then page with "Category list" is shown

