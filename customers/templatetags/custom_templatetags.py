from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def space2Dash(s):
    return s.replace('e', '_');

@register.filter
def int_sum(list):
    return int(l.get('customer_phone_number') for l in list) 

@register.filter
def str_sum(list):
    return "".join(list)
