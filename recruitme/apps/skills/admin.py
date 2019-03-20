from django.contrib import admin

from .models import Skill, SkillRelation

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'created_on', 'modified_on', 'created_by')
    exclude = ('created_by',)

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(SkillAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.created_by.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Skill.objects.all()
        return Skill.objects.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class SkillRelationAdmin(admin.ModelAdmin):
    list_display = ('skill', 'created_on', 'modified_on', 'created_by')
    exclude = ('created_by',)

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(SkillRelationAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.created_by.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return SkillRelationAdmin.objects.all()
        return SkillRelationAdmin.objects.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillRelation, SkillRelationAdmin)
