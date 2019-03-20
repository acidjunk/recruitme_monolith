from django.conf.urls import patterns, url

from .views import DeveloperList, DeveloperDetail, ProjectCreate, ProjectUpdate


urlpatterns = patterns(
    '',
    url(r'^$', DeveloperList.as_view(), name='developer-list'),
    url(r'^(?P<developer_id>\d+)/$', DeveloperDetail.as_view(), name='developer-detail'),
    url(r'^(?P<slug>[-\w\d]+)/$', DeveloperDetail.as_view(), name='developer-detail'),
    url(r'^project/new/$', ProjectCreate.as_view(), name='project-new'),
    url(r'^project/(?P<project_id>\d+)/$', ProjectUpdate.as_view(), name='project-update'),
    url(r'^project/(?P<slug>[-\w\d]+)/$', ProjectUpdate.as_view(), name='project-update'),

)