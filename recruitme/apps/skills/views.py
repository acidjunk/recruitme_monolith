from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from .models import Skill, SkillRelation
from .forms import SkillForm


def skill_cloud(request):
    skills = Skill.objects.all()
    skill_list = []
    for skill in skills:
        skill_list.append((skill.skill, len(skill.tagged_items.all())))
    context_dict = {'skill_list': skill_list}
    return render(request, 'tagger/tag_cloud.html', context_dict)


@login_required
def add_skill(request, model, model_id):
    # Set nice return URL
    return_url = request.session.get('tagger_return_url', None)
    if not return_url:
        request.session['tagger_return_url'] = request.META.get('HTTP_REFERER')

    user = request.user
    content_type = ContentType.objects.get(model=model)

    if request.method == 'POST':
        new_skill = request.POST.get('new_skill', None)
        skill = request.POST.get('skill', None)
        if new_skill:
            skill = Skill(skill=new_skill, created_by=user)
            skill.save()
            skill_relation = SkillRelation(content_type=content_type, object_id=model_id)
            skill_relation.created_by = user
            skill_relation.skill = skill
            skill_relation.save()
        elif skill:
            skill = Skill.objects.get(id=skill)
            skill_relation = SkillRelation(content_type=content_type, object_id=model_id)
            skill_relation.created_by = user
            skill_relation.skill = skill
            skill_relation.save()

    form = SkillForm()
    skills = SkillRelation.objects.filter(content_type=content_type, object_id=model_id)
    form.fields["skill"].queryset = Skill.objects.exclude(skill__in=[o.skill for o in skills])

    context_dict = {'form': form, 'skills': skills}
    return render(request, 'skills/add_skill.html', context_dict)


@login_required
def go_back(request):
    return_url = request.session.get('add_skill_return_url', None)
    if return_url:
        del request.session['add_skill_return_url']
        return redirect(return_url)
    else:
        # No return URL? This shouldn't happen. Anyway let's return to home
        return redirect('/')


@login_required
def delete_skill(request, id):
    skill_relation = SkillRelation.objects.get(id=id)
    find_all_skill_relations = SkillRelation.objects.filter(skill=skill_relation.skill)
    if find_all_skill_relations.count() == 1:
        skill = Skill.objects.get(id=skill_relation.tag_id)
        skill.delete()
    else:
        skill_relation.delete()
    return redirect(request.META.get('HTTP_REFERER'))
