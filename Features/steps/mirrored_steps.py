from behave import *
from sample.mirrored import Mirrored
from assertpy import *

mirrored = Mirrored()


@given("two words")
def step_impl(context):
    context.data = context.text.replace('\r', '').split(",")


@when("they are mirrored and same length")
def step_impl(context):
    context.result = mirrored.game(context.data[0], context.data[1])


@then("returned value should be True")
def step_impl(context):
    assert_that(context.result).is_equal_to(True)


@when("they are not mirrored and same length")
def step_impl(context):
    context.result = mirrored.game(context.data[0], context.data[1])


@then("returned value should be False")
def step_impl(context):
    assert_that(context.result).is_equal_to(False)


@when("they are not mirrored and first is longer")
def step_impl(context):
    context.result = mirrored.game(context.data[0], context.data[1])


@then("returned value should be \"Words aren't the same length\"")
def step_impl(context):
    assert context.result == "Words aren't the same length"


@when("they are not mirrored and second is longer")
def step_impl(context):
    context.result = mirrored.game(context.data[0], context.data[1])


@when("they are not mirrored and first is an int")
def step_impl(context):
    context.result = mirrored.game(int(context.data[0]), context.data[1])


@then("returned value should be \"Cannot be an integer\"")
def step_impl(context):
    assert context.result == "Cannot be an integer"


@when("they are not mirrored and second is an int")
def step_impl(context):
    context.result = mirrored.game(context.data[0], int(context.data[1]))


@when("they are not mirrored and first is boolean")
def step_impl(context):
    context.result = mirrored.game(bool(context.data[0]), context.data[1])


@then("returned value should be \"Must be a string\"")
def step_impl(context):
    assert context.result == "Must be a string"


@when("they are not mirrored and second is boolean")
def step_impl(context):
    context.result = mirrored.game(context.data[0], bool(context.data[1]))
