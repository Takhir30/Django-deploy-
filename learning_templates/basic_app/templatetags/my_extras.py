from django import template

register = template.Library()


@register.filter
def cu(value, arg):
    return value.replace(arg, '')
