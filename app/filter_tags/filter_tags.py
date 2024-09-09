from django import template
from app import helpers
register = template.Library()

@register.filter
def join(string_1, string_2):
    return f'{string_1}{string_2}'

@register.filter
def age(string_1):
    age = helpers.year_calculator(string_1)
    return f'{age}'