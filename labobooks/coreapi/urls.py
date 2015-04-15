from django.conf.urls import include, url

from rest_framework import routers

from coreapi import views


router = routers.DefaultRouter()
router.register(r'mybook', views.MyBookViewSet)
router.register(r'bookinfo', views.BookInfoViewSet)


urlpatterns = [
    url(r'^data/v1/', include(router.urls)),
    url(r'^info/v1/search', 'coreapi.views.search_bookinfo', name='search_bookinfo'),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
