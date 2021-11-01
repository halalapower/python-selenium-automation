# Created by ladyh at 10/10/2021
Feature: Test scenario for amazon privacy notice
  user can open amazon window and click on privacy notice linkScenario: User can open and close Amazon Privacy Notice


  Given open amazon tc page
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window and switch back to original


