from django.template import Library

register = Library()


@register.filter(name='get_private_key')
def get_private_key(d, k):
    return d.get(k, None)
