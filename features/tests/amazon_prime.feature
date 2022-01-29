# Created by ladyh at 11/2/2021
Feature: Amazon Prime tests

  Scenario: Verify user sees correct amount of benefit boxes
    Given Open Amazon Prime
    Then Verify 3 benefit boxes are present