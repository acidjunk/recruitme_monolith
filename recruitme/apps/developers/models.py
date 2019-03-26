from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date

from django.conf import settings

@python_2_unicode_compatible
class Developer(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(unique=True)
    birth_date = models.DateField()
    bio = models.TextField()
    city = models.CharField(max_length=128)  # Todo implement location stuff
    is_public = models.BooleanField(default=False)
    profile_title = models.CharField(max_length=255)
    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    created_by = models.ForeignKey(User, related_name='developer_created_by')
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_by = models.ForeignKey(User, related_name='developer_modified_by')
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        get_latest_by = 'created_on'
        ordering = ('-created_on',)
        verbose_name = 'developer'

    def __str__(self):
        return self.slug

    def age(self):
        today = date.today()
        delta = relativedelta(today, self.birth_date)
        return str(delta.years)

class Project(models.Model):
    developer = models.ForeignKey(Developer, related_name='developer')
    language = models.CharField(choices=settings.LANGUAGES, max_length=20)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start = models.DateField()
    is_ended = models.BooleanField(default=False)
    end = models.DateField(blank=True, null=True)
