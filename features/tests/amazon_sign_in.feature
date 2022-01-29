# Created by ladyh at 11/4/2021
  Feature: test for sign in button
  Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened