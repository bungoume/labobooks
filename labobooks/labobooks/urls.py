from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('coreapi.urls')),
    url(r'^', include('webfront.urls')),
    url(r'^accounts/', include('account.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
]
