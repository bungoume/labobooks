from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('coreapi.urls')),
    url(r'^accounts/', include('accountapp.urls')),
    url(r'^accounts/', include('account.urls')),
    # url(r'^accounts/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^', include('webfront.urls')),
]
