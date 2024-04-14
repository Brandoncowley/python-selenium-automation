Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: Verify user can see product names and images
    Given Open Target main page
    When Search for Apple Air Pods
    Then Verify that every product has a name and an image