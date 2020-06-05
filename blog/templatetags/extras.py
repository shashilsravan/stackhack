from datetime import datetime
from django import template
import random
register = template.Library()


@register.filter
def days_until(date):
    delta = datetime.date(date) - datetime.now().date()
    return delta.days

@register.filter
def random_mine(lis):
    return random.choice(lis)