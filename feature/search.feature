Feature: buying and searching for a product

        Background:
          Given web browser is on the home page

    Scenario Outline: 19. searching for an existing product via the Search bar
      Given the <product> exists
      When user searches for a <product>
      Then page with <product> is shown
        Examples:
          | product                  |
          | Apple Cinema 30"         |
          | iMac                     |
          | Samsung SyncMaster 941BW |
          | Samsung Galaxy Tab 10.1  |
          | HTC Touch HD             |
          | iPhone                   |
          | Palm Treo Pro            |
          | Canon EOS 5D             |
          | Nikon D300               |
          | HP LP3065                |
          | HTC Touch HD             |
          | iPod Classic             |
          | MacBook                  |
          | MacBook Air              |

    Scenario: 20. searching for a non existing product via the Search bar
      Given the product does not exist
      When user searches for a not-product
      Then page with no-matched-product text

    Scenario: 21. adding a product to cart
      Given the product exist
      When user clicks on "Add to Cart"
      Then product should be added to cart

    Scenario: 22. buying a product that is already in cart
      Given a web browser is on "Shopping Cart" page
      When user clicks on "Checkout"
      Then page with "Checkout" is shown

    Scenario: 23. confirming order
      Given a web browser is on "Checkout" page
      And personal information is filled out
      And shipping method is filled out
      And payment method is filled out
      When user clicks on "Confirm Order"
      Then page with "Your order has been placed!" is shown
