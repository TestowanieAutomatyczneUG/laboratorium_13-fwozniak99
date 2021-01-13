from behave import *
from sample.planets import Planets


def before_scenario(context, scenario):
    if 'planets' in scenario.feature.tags:
        context.planet = Planets()
        print("before scenario")


def after_scenario(context, scenario):
    if 'planets' in scenario.feature.tags:
        context.planet = None
        print("\nafter scenario\n")
