from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
       url(r'^skill-cloud$', views.skill_cloud, name='skill-cloud'),
       url(r'^add-skill/(?P<model>\w+)/(?P<model_id>\d+)$', views.add_skill, name='add_skill'),
       url(r'^skill/delete/(?P<id>\d+)$', views.delete_skill, name='delete-skill'),
       url(r'^go-back$', views.go_back, name='go-back'),
)
