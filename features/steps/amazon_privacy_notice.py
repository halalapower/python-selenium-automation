from behave import *

use_step_matcher("re")


@given("Open Amazon T&C page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Open Amazon T&C page')


@when("Store original windows")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Store original windows')


@step("Click on Amazon Privacy Notice link \(\*see image below\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Click on Amazon Privacy Notice link (*see image below)')


@step("Switch to the newly opened window")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Switch to the newly opened window')


@then("Verify Amazon Privacy Notice page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify Amazon Privacy Notice page is opened')


@step("User can close new window and switch back to original")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And User can close new window and switch back to original')