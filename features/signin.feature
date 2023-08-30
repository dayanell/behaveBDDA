@regression @smoke
Feature: User sign-in

  Background:
    Given the user navigate to conduit sign-in page

  Scenario Outline: Successful sign-in
    Given The user validate the page title
    When the user fills in the form with "<email>" "<password>"
    Then the user should see "<username>" on the page
    Examples: User data
      | email                     | password  | username  |
      | 16test@test.com.com.bv    | test@test | Josh Doe  |

  Scenario Outline: unsuccessful sign-in
  Given The user validate the page title
  When the user fills in the form with "<email>" "<password>"
  Then the user should see error message on the page
  Examples: User data
    | email                     | password  |
    | 16test@test.com.com.bv    | None      |
    | None                      | 123456    |
    | hjgkhjgh@bnbnbjjj         | 123456    |
    | 16test@test.com.com.bv    | 12345     |
    | 16test@test.com.com.bv    | test@test |




