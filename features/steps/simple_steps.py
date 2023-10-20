from behave import given, when, then


@given("this simple thing")
def step_impl(context):
    pass
    # raise NotImplementedError("STEP: Given this simple thing")


@when("this happens")
def step_impl1(context):
    pass
    # raise NotImplementedError("STEP: When this happens")


@then("this is expected")
def step_impl2(context):
    pass
    # raise NotImplementedError("STEP: Then this is expected")
