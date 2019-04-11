# -*- coding: UTF-8 -*-

from django.db import models
from django import template

register = template.Library()

@register.tag
def get_objects(parser, token):
    """
    Gets a queryset of objects of the model specified by app and model names

    Usage:

        {% get_objects [<manager>.]<method> from <app_name>.<model_name> [limit <amount>] as <var_name> %}

    Example:

        {% get_objects latest_published from people.Person limit 3 as people %}
        {% get_objects all from dci.Task limit 3 as tasks %}
        {% get_objects site_objects.all from articles.Article as articles %}

    """
    amount = None
    try:
        tag_name, manager_method, str_from, appmodel, str_limit, amount, str_as, var_name = token.split_contents()
    except ValueError:
        try:
            tag_name, manager_method, str_from, appmodel, str_as, var_name = token.split_contents()
        except ValueError:
            raise template.TemplateSyntaxError(
                "get_objects tag requires a following syntax: {% get_objects <manager_method> from <app_name>.<model_name> limit <amount> as <var_name> %}")
    try:
        app_name, model_name = appmodel.split(".")
    except ValueError:
        raise template.TemplateSyntaxError(
            "get_objects tag requires application name and model name separated by a dot")
    model = models.get_model(app_name, model_name)
    return ObjectsNode(model, manager_method, amount, var_name)


class ObjectsNode(template.Node):
    def __init__(self, model, manager_method, amount, var_name):
        self.model = model
        self.manager_method = manager_method
        self.amount = amount
        self.var_name = var_name

    def render(self, context):
        if "." in self.manager_method:
            manager, method = self.manager_method.split(".")
        else:
            manager = "_default_manager"
            method = self.manager_method

        qs = getattr(
            getattr(self.model, manager),
            method,
            self.model._default_manager.none,
        )()
        if self.amount:
            amount = template.resolve_variable(self.amount, context)
            context[self.var_name] = qs[:amount]
        else:
            context[self.var_name] = qs
        return ''
