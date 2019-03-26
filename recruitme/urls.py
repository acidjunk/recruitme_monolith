from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = patterns('',
    url(r'', include('django.contrib.auth.urls')),
    #url(r'', include('django.contrib.auth.urls', namespace='auth')), # Could be needed for social login
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$',include('recruitme.apps.static_page.urls', namespace='page')),  # home
    url(r'^page/', include('recruitme.apps.static_page.urls', namespace='page')),  # other static pages
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^social/', include('recruitme.apps.social_login.urls', namespace='social_login')),
    url(r'^skills/', include('recruitme.apps.skills.urls', namespace='skills')),
    url(r'^developers/', include('recruitme.apps.developers.urls', namespace='developers')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('recruitme.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
)
