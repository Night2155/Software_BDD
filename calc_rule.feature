@Web @Calculator
Feature: Web Calculator
  As a engineer,
  In order to meet the requirements of my client,
  I have to do arithmetic Calculator.

  Background:
    The Calculator page is displayed

  Scenario: commutative property
    When I enter "3 + 4" first
    And I enter "4 + 3" again
    Then I get the same answer

  Scenario: associative property
    When I enter "(2 + 3) + 4" first
    And I enter "3 + (2 + 4)" again
    Then I get the same answer

  Scenario: distributive property
    When I enter "2 * (1 + 3)" first
    And I enter "(2*1) + (2*3)" again
    Then I get the same answer