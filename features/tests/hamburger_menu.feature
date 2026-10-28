# Created by ladyh at 9/27/2021
Feature: Hamburger menu tests
  # Enter feature description here

  Scenario: Users can see hamburger menu
    Given Open Amazon page
    When Input coffee into Amazon search
    When Click on Amazon search icon
    Then Verify hamburger menu is present