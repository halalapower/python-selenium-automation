# Created by ladyh at 9/27/2021
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a coffee on Amazon
    Given Open Amazon page
    When Input coffee into amazon search
    When Click on Amazon search icon
    Then Verify "coffee" text is shown


  Scenario: User can select blouse color
    Given Open Amazon product blouse page
    Then Verify user can click through color

Scenario: User can add product to the cart
    Given Open Amazon page
    When Input 3-Quat Tritan farm to table pitcher into amazon search
    When Click on Amazon search icon
    When Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item\s\
    Then Verify cart has correct product

