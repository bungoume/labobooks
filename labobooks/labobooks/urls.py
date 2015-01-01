from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('coreapi.urls')),
    url(r'^', include('webfront.urls', namespace='webfront')),
    url(r'^accounts/', include('account.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
