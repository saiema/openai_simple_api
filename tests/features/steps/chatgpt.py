from typing import Dict

from behave import *

from api.ChatGPT import ChatGPT

use_step_matcher("re")


@when("the ChatGPT API manager is initialized with no arguments")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.chatgpt_api = ChatGPT.instance()
    context.chatgpt_api.reset_to_defaults()


@then("the ChatGPT API manager must have the following configuration")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for row in context.table:
        config_key: str = row['config_key']
        expected_value = row['value']
        obtained_value = getattr(context.chatgpt_api, config_key)
        assert f"expected {expected_value}, but got {obtained_value} instead", expected_value == obtained_value


@given("the ChatGPT API manager is initialized with no arguments")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.chatgpt_api = ChatGPT.instance()
    context.chatgpt_api.reset_to_defaults()


@given("the ChatGPT API manager secret api key is set to the configured secret key")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.chatgpt_api.secret_key(context.config.secret_key())


@step("available models are requested from the ChatGPT API manager")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.available_models = context.chatgpt_api.available_models


@then("the available models returned must include the following models")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    for expected_model in context.table.rows:
        assert f"expected model {expected_model} was not returned by the ChatGPT api", (
                expected_model in context.available_models)


@step("the model of the ChatGPT API manager is set to \"(?P<model>.+)\"")
def step_impl(context, model: str):
    """
    :param model: str
    :type context: behave.runner.Context
    """
    context.chatgpt_api.model = model


@when('a completion is requested for the prompt (?P<prompt>.*)')
def step_impl(context, prompt: str):
    """
    :param prompt:
    :type context: behave.runner.Context
    """
    context.completion_obtained = context.chatgpt_api.completion(prompt)
    print(f"Completion obtained is {context.completion_obtained} using model {context.chatgpt_api.model}")


@then('the obtained completion will be (?P<completion>.*)')
def step_impl(context, completion: str):
    """
    :param completion:
    :type context: behave.runner.Context
    """
    completion_choices: Dict = context.completion_obtained.choices
    assert "Expecting at least 1 completion, but got none.", len(completion_choices) >= 1
    expected_completion_found: bool = False
    for completion_obtained in completion_choices:
        if completion == completion_obtained:
            expected_completion_found = True
            break
    assert f"Was expecting {completion}, got {completion_choices} instead", expected_completion_found
