@Web @Calculator
Feature: Web Calculator
  As a engineer,
  In order to meet the requirements of my client,
  I have to do arithmetic Calculator.

  Scenario: User enter case 3 + 2 = 5
    Given I enter "3 + 2"

    When I press "=" button
    Then I get the answer "5"

  Scenario: User enter case 9 - 5 = 4
    Given I enter "9 - 5"

    When I press "=" button
    Then I get the answer "4"

  Scenario: User enter case 5 * 2 = 10
    Given I enter "5 * 2"

    When I press "=" button
    Then I get the answer "10"

  Scenario: User enter case 15 / 3 = 5
    Given I enter "15 / 3"

    When I press "=" button
    Then I get the answer "5"

  Scenario: User enter case 3 -+*/ 2 = Invalid Input
    Given I enter "3 -+*/ 2"

    When I press "=" button
    Then I get the answer "Invalid Input"

  Scenario: User enter case hello world = Invalid Input
    Given I enter "hello world"

    When I press "=" button
    Then I get the answer "Invalid Input"