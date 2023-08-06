from behave import *

from api.PromptManager import PromptManager

use_step_matcher("re")


@Given("that the prompt manager is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.prompt_manager = PromptManager.instance()


@step("the prompt manager custom prompts are reset")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.prompt_manager.clear_custom_prompts()


@step("there should not be any custom prompt available")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert not context.prompt_manager.custom_prompts()


@then("a new prompt manager is available")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.prompt_manager is not None


@when("pre-defined prompts are requested from the prompt manager")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.predefined_prompts = context.prompt_manager.predefined_prompts()


@then("the following prompts must be obtained")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected_prompts: [str] = []
    for row in context.table.rows:
        for expected_prompt in row:
            expected_prompts.append(expected_prompt)
    assert context.predefined_prompts == expected_prompts


@step("the prompt manager does not hold any custom prompt")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert not context.prompt_manager.custom_prompts()


@when("the custom prompt (?P<prompt>.+) is added to the prompt manager")
def step_impl(context, prompt):
    """
    :type context: behave.runner.Context
    :type prompt: str
    """
    context.prompt_manager.select_prompt(prompt)


@then("the custom manager should contain (?P<contain>.+) the custom prompt (?P<prompt>.+)")
def step_impl(context, contain, prompt):
    """
    :type context: behave.runner.Context
    :type contain: str
    :type prompt: str
    """
    should_be_contained: bool = bool(contain)
    assert (prompt in context.prompt_manager.custom_prompts()) == should_be_contained


@when("the following custom prompts are added to the prompt manager")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for custom_prompt in context.table.rows:
        context.prompt_manager.select_prompt(custom_prompt)


@then('the prompt manager must have (?P<saved_prompts>.+) custom prompts saved')
def step_impl(context, saved_prompts: int):
    """
    :param saved_prompts:
    :type context: behave.runner.Context
    """
    obtained_saved_prompts = len(context.prompt_manager.custom_prompts())
    assert f"Expected {saved_prompts}, got {obtained_saved_prompts} instead.", obtained_saved_prompts == saved_prompts


@step('the last custom prompt in the prompt manager must be (?P<last_custom_prompt>.*)')
def step_impl(context, last_custom_prompt: str):
    """
    :param last_custom_prompt:
    :type context: behave.runner.Context
    """
    obtained_last_added_custom_prompt = context.prompt_manager.last_selected_prompt()
    assert f"Expected {last_custom_prompt}, obtained {obtained_last_added_custom_prompt} instead.",(
            obtained_last_added_custom_prompt == last_custom_prompt)
