from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import SkillRelation

register = template.Library()


def show_skills(model, pk):
    object_type = ContentType.objects.get(model=model)
    skill_relations = SkillRelation.objects.filter(content_type=object_type.id, object_id=pk)
    return {'skill_relations': skill_relations, 'model': model, 'pk': pk}


register.inclusion_tag('skills/templatetags/show_skills.html')(show_skills)
