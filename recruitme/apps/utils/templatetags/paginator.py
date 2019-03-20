from django import template

register = template.Library()

def paginator(queryset, request=None):
    return { 'queryset': queryset, 'request': request }

register.inclusion_tag('paginator.html')(paginator)