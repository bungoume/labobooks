from django.conf.urls import include, url

from rest_framework import routers

from coreapi import views


router = routers.DefaultRouter()
router.register(r'bookinfo', views.BookInfoViewSet)


urlpatterns = [
    url(r'^data/v1/mybook', views.MyBookViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'delete': 'destroy'})),
    url(r'^data/v1/', include(router.urls)),
    url(r'^info/v1/search', views.amazon_search, name='search_books'),
    url(r'^info/v1/(?P<isbn>[\d]{13})/?', views.amazon_search, name='search_books'),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
