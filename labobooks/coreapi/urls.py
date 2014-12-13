from django.conf.urls import patterns, include, url

from rest_framework import routers

# from coreapi import views


router = routers.DefaultRouter()
# router.register(r'xxx', views.XXXViewSet)

urlpatterns = patterns(
    '',
    url(r'^data/v1/', include(router.urls)),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
