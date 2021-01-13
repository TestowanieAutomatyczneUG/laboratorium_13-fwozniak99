from behave import *
from sample.planets import Planets

"""
@given("we have an instance of Planets")
def step_impl(context):
    context.planet = Planets()
"""

@when("the planet is Ziemia and the time is 1000000000 seconds")
def step_impl(context):
    context.result = context.planet.game(1000000000, "Ziemia")


@then("returned age will be 31.69")
def step_impl(context):
    assert context.result == 31.69


@when("the planet is Merkury and the time is 2134835688 seconds")
def step_impl(context):
    context.result = context.planet.game(2134835688, "Merkury")


@then("returned age will be 280.88")
def step_impl(context):
    assert context.result == 280.88


@when("the planet is Wenus and the time is 123456789 seconds")
def step_impl(context):
    context.result = context.planet.game(123456789, "Wenus")


@then("returned age will be 6.36")
def step_impl(context):
    assert context.result == 6.36


@when("the planet is Mars and the time is 987654321 seconds")
def step_impl(context):
    context.result = context.planet.game(987654321, "Mars")


@then("returned age will be 16.64")
def step_impl(context):
    assert context.result == 16.64


@when("the planet is Jowisz and the time is 555555555 seconds")
def step_impl(context):
    context.result = context.planet.game(555555555, "Jowisz")


@then("returned age will be 1.48")
def step_impl(context):
    assert context.result == 1.48


@when("the planet is Saturn and the time is 666666666 seconds")
def step_impl(context):
    context.result = context.planet.game(666666666, "Saturn")


@then("returned age will be 0.72")
def step_impl(context):
    assert context.result == 0.72


@when("the planet is Uran and the time is 9999999999 seconds")
def step_impl(context):
    context.result = context.planet.game(9999999999, "Uran")


@then("returned age will be 3.77")
def step_impl(context):
    assert context.result == 3.77


@when("the planet is Neptun and the time is 8888888888 seconds")
def step_impl(context):
    context.result = context.planet.game(8888888888, "Neptun")


@then("returned age will be 1.71")
def step_impl(context):
    assert context.result == 1.71
