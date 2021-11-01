# Created by ladyh at 11/1/2021
Feature: test for bestsellers functionality
  # Enter feature description here

  Scenario: There are 5 bestsellers links
    Given Open Amazon Bestsellers
    Then Verify there are 5 links

  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page