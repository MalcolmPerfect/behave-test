"""Steps that align to the simple feature. Mainly just for trying out
different features in behave, handling params etc.
"""
import logging
from behave import given, when, then


@given("this simple thing")
def step_impl(context):
    pass


@when("this happens")
def step_impl1(context):
    pass


@then("this is expected")
def step_impl2(context):
    pass


@given("there are {gherkins_total:Number} gherkins")
def step_total_gherkins(context, gherkins_total: int):
    """purpose of this was try out using parse to turn a param from a string to an
    int. Useful if need to convert things repeatedly versus repetition of
    int() or using strings inappropriately"""
    context.gherkins_total = gherkins_total
    logging.info(f"gherkins_total {gherkins_total} {type(gherkins_total)}")


@when("I eat {gherkins_eaten:Number} gherkins")
def step_eaten_gherkins(context, gherkins_eaten: int):
    context.gherkins_eaten = gherkins_eaten
    pass
    # raise NotImplementedError(u'STEP: When Rex eats 88 gherkins')


@then("there are {gherkins_remaining:Number} gherkins left")
def step_validate_gherkins(context, gherkins_remaining: int):
    assert gherkins_remaining == (context.gherkins_total - context.gherkins_eaten)
