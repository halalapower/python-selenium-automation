# Created by ladyh at 9/25/2021
Feature: Test Scenario to Cancel Order
  # Enter feature description here

  Scenario: User can cancel order on input box
    Given Open Amazon cancel page
    When Input Cancel Order into search field
    And Click on search icon
    Then Product results for Cancel Order  are shown

