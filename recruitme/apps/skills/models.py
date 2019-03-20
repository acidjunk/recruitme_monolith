from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


@python_2_unicode_compatible
class Skill(models.Model):
    skill = models.SlugField(unique=True)

    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        get_latest_by = 'created_on'
        ordering = ('skill',)
        verbose_name = 'skill'

    def __str__(self):
        return self.skill


@python_2_unicode_compatible
class SkillRelation(models.Model):
    skill = models.ForeignKey(Skill, related_name='skill_relation')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        get_latest_by = 'created_on'
        ordering = ('skill',)
        verbose_name = 'skill relation'

    def __str__(self):
        return 'Model:%s, ID:%s, Skill:%s' % (self.content_type, self.object_id, self.skill.skill)
