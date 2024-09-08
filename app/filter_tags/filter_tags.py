from django import template

register = template.Library()

@register.filter
def join(string_1, string_2):
    return f'{string_1}{string_2}'