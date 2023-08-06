# Created by stein at 8/2/23
Feature: ChatGPT API configuration and queries
  The system must allow to configure a ChatGPT API manager with settings such as:
    * Which model to use.
    * Secret key to use.
    * Maximum tokens for input and output.
    * How many responses to return
      (when more than one response is available for a particular query).
  The system must also allow to execute the following actions on the ChatGPT API manager:
    * List available models.
    * Make a query from a prompt followed by a text.

  Scenario: ChatGPT API manager default initialization
    When the ChatGPT API manager is initialized with no arguments
    Then the ChatGPT API manager must have the following configuration
    | config_key  | value         |
    | model       | gpt-3.5-turbo |
    | max_tokens  | 16            |
    | temperature | 1             |
    | n           | 1             |
    | best_of     | 1             |

  Scenario: ChatGPT API manager list models must include gpt-3 related models
    Given the ChatGPT API manager is initialized with no arguments
    And the ChatGPT API manager secret api key is set to the configured secret key
    When available models are requested from the ChatGPT API manager
    Then the available models returned must include the following models
    | model                   |
    | gpt-3.5-turbo           |
    | gpt-3.5-turbo-16k       |
    | gpt-3.5-turbo-0613      |
    | gpt-3.5-turbo-16k-0613  |
    | text-davinci-003        |
    | text-davinci-002        |
    | code-davinci-002        |

  Scenario: ChatGPT API manager correctly respond to a prompt
    Given the ChatGPT API manager is initialized with no arguments
    And the ChatGPT API manager secret api key is set to the configured secret key
    And the model of the ChatGPT API manager is set to "text-davinci-003"
    When a completion is requested for the prompt "could you give an answer by yes or no?"
    Then the obtained completion will be "Yes."
