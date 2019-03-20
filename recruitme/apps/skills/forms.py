from django.forms import ModelForm

from .models import SkillRelation


class SkillForm(ModelForm):

    class Meta:
        model = SkillRelation
        fields = ['skill']
