# Importing the template module from Django
from django import template

# Creating an instance of the template library
register = template.Library()


# Defining a custom filter named 'calc_subtotal'
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
