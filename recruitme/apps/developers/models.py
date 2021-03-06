from __future__ import unicode_literals

import requests
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
    bitbucket_profile = models.URLField(blank=True)
    bitbucket_repo_info = models.TextField(blank=True)
    bio = models.TextField()
    city = models.CharField(max_length=128)  # Todo implement location stuff
    is_public = models.BooleanField(default=False)
    profile_title = models.CharField(max_length=255)
    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    github_repo_info = models.TextField(blank=True)
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

    def update_github_repo_info(self):
        github_user = self.github_profile.split("/")[-1]
        response = requests.get('https://api.github.com/users/{owner}/repos'.format(owner=github_user))
        if response.status_code == 200:
            json = response.json()
            self.github_repo_info = json
            self.save()

    def update_bitbucket_repo_info(self):
        bitbucket_user = self.bitbucket_profile.split("/")[-1]
        response = requests.get(
            'https://bitbucket.org/api/2.0/repositories/{owner}'.format(
                owner=bitbucket_user))
        if response.status_code == 200:
            json = response.json()
            if json.get('next'):
                raise NotImplementedError('Sry pagination was not in scope')
            self.bitbucket_repo_info = json.get('values', [])
            self.save()

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
