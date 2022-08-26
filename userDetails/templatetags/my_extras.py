from django import template
register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all the values.
    """
    return value.replace(arg,'')
#register.filter('cut',cut)
