# Created by ladyh at 9/27/2021
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input coffee into search field
    And Click on search icon
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: User can select blouse color
    Given Open Amazon product blouse page
    Then Verify user can click through color