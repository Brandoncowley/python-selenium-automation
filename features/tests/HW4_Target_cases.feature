# Created by brandon at 3/2/24
Feature: Target UI tests and add item to cart

   Scenario: Target Circle page has correct amount of Benefit Boxes
    Given Open Target Circle page
    Then Verify Circle Benefits are present
    And Verify page has 5 Benefits boxes

   Scenario: Add product to cart
     Given Open Target page
     When Search for chair
     And Add item to cart
     Then Verify item added to cart

  Scenario: Verify UI elements on Target Help page
    Given Open Target Help page
    Then Verify UI elements are present
    And Verify first Help section has 7 elements