from django import template

# option 1: one way to register your filter
register = template.Library()

@register.filter(name='cut')
def cuts(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# this is also part of option 1
# register.filter('cut',cuts)
