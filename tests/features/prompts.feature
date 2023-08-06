# Created by stein at 8/1/23
Feature: Prompt selection
  The system must provide several pre-defined prompts, and the
  ability to create and save new custom prompts.

  Scenario: Prompt manager initialization
    Given that the prompt manager is created
    And the prompt manager custom prompts are reset
    When pre-defined prompts are requested from the prompt manager
    Then the following prompts must be obtained
      | prompt |
      | Translate the following text |
      | Correct the syntax of the following text |
      | List some prompts based on the following text (WUUUT?) |
    And there should not be any custom prompt available

  Scenario Outline: Prompt manager custom prompts
    Given that the prompt manager is created
    And the prompt manager custom prompts are reset
    When the custom prompt <prompt> is added to the prompt manager
    Then the custom manager should contain <contain> the custom prompt <prompt>

    Examples:
      | prompt                       | contain |
      | Sing me a song               | True    |
      | Translate the following text | False   |

  Scenario: Prompt manager last added custom prompt
    Given that the prompt manager is created
    And the prompt manager custom prompts are reset
    When the following custom prompts are added to the prompt manager
    | prompt  |
    | sugar   |
    | oh      |
    | honey   |
    | honey   |
    Then the prompt manager must have "3" custom prompts saved
    And the last custom prompt in the prompt manager must be "honey"

