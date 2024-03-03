# Created by brandon at 3/2/24
Feature: Main page UI tests for Target

  Scenario: Header has the correct amount of links
    Given Open Target Circle page
    Then Verify header is present
    And Verify page has 5 Benefits boxes