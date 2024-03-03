# Created by brandon at 2/19/24
Feature: Test scenarios for Target website

  Scenario: User can see empty cart message
    Given Open Target page
    When Click on Cart icon
    Then Verify empty cart


  Scenario: User can access Sign in form
    Given Open Target page
    When Click on Sign in
    And Click Sign in on side menu
    Then Verify Sign in form opens


Scenario: User can search for product
  Given Open Target page
  When Search for pillow
  Then Verify pillow in search results
