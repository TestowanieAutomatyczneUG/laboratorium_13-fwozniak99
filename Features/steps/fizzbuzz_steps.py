from behave import *
from sample.fizzbuzz import FizzBuzz


@given("we have an instance of FizzBuzz")
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when("the number is 15")
def step_impl(context):
    context.result = context.fizzbuzz.game(15)


@then("returned value will be FizzBuzz")
def step_impl(context):
    assert context.result == "FizzBuzz"


@when("the number is 5")
def step_impl(context):
    context.result = context.fizzbuzz.game(5)


@then("returned value will be Buzz")
def step_impl(context):
    assert context.result == "Buzz"


@when("the number is 3")
def step_impl(context):
    context.result = context.fizzbuzz.game(3)


@then("returned value will be Fizz")
def step_impl(context):
    assert context.result == "Fizz"


@when("the number is 4")
def step_impl(context):
    context.result = context.fizzbuzz.game(4)


@then("returned value will be 4")
def step_impl(context):
    assert context.result == "4"


@when("the number is {number}")
def step_impl(context, number):
    context.result = context.fizzbuzz.game(int(number))


@then("returned value will be {result}")
def step_impl(context, result):
    assert context.result == result

