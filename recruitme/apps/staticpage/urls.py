from django.conf.urls import patterns, url

from .views import page

urlpatterns = patterns('',
    # ex: /page/slugname
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    # ex: /page
    url(r'^$', page, name='home'),
)