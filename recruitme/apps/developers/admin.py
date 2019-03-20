from django.contrib import admin

from .models import Developer, Project

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('slug', 'bio', 'age', 'modified_on', 'created_on')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start', 'end', 'is_ended')

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)
