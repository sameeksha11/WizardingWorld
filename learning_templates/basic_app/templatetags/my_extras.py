from django import template


register= template.Library()

@register.filter(name='cut')
def cut(value,arg):
    '''
    this cuts value of arg from string!
    '''
    return value.replace(arg,'')
