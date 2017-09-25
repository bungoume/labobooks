# from amazon.api import AmazonAPI
import bottlenose
from cachetools import cached, TTLCache
import xmltodict

from django.conf import settings
from django.http import JsonResponse

from rest_framework import status, viewsets
from rest_framework.response import Response
import requests


from core.models import MyBook, BookInfo
from coreapi.drippers import amazon_dripper
from coreapi.serializers import MyBookSerializer, BookInfoSerializer


amazon = bottlenose.Amazon(
    settings.AMAZON_PRODUCT_ADVERTISING_ID,
    settings.AMAZON_PRODUCT_ADVERTISING_SECRET,
    settings.AMAZON_ASSOCIATE_TAG,
    Region=settings.AMAZON_ASSOCIATE_REGION,
    MaxQPS=0.9)

amazon_cache = TTLCache(256, ttl=3600)


class MyBookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyBook.objects.all()
    serializer_class = MyBookSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        orgs = request.user.org_memberships
        try:
            org = orgs.get(id_slug=request.query_params.get('org'))
        except:
            org = orgs.all()
        queryset = queryset.filter(organization__in=org)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # FIXME: 権限チェック
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        orgs = request.user.org_memberships
        try:
            org = orgs.get(id_slug=request.query_params.get('org'))
        except:
            org = orgs.last()
        data = request.data.copy()
        data['organization'] = org.id
        data['book_info'] = data['isbn']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


def amazon_search(request):
    keyword = request.GET.get('keyword') or 'Python'
    # http://webservices.amazon.co.jp/scratchpad/index.html

    @cached(amazon_cache)
    def fetch(keyword):
        # amazon-apiは500エラー返しがちなので3回トライする
        retry = 3
        while retry:
            try:
                res = amazon.ItemSearch(
                    Keywords=keyword,
                    SearchIndex="Books",
                    ResponseGroup="Images,ItemAttributes"
                )
                data = xmltodict.parse(res)
                return data
            except:
                retry -= 1
                if retry <= 0:
                    raise
    data = fetch(keyword)
    data = amazon_dripper(data)
    # isbn_list = [x["isbn"] for x in data['items']]
    # r = requests.get(settings.OPENBD_API, params={'isbn': ','.join(isbn_list)})
    # data = openbd_dripper(r.json())

    for item in data['items']:
        BookInfo(**item).save()

    return JsonResponse(data)

# https://openbd.jp/


def google_search(request):
    GOOGLE_APH_PATH = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': request.GET.get('keyword', ''),
        'orderBy': 'newest',
    }
    r = requests.get(GOOGLE_APH_PATH, params=params)
    return JsonResponse(r.json())


def rakuten_search(request):
    RAKUTEN_API_PATH = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404'
    params = {
        'applicationId': settings.RAKUTEN_APPLICATION_ID,
        'format': 'json',
        'formatVersion': 2,
        'sort': 'sales',
        # 'elements': 'title,seriesName,author,publisherName,salesDate,mediumImageUrl,isbn',
    }

    keyword = request.GET.get('keyword', '')
    if keyword:
        params['title'] = keyword
    else:
        # https://app.rakuten.co.jp/services/api/BooksGenre/Search/20121128?booksGenreId=001
        params['booksGenreId'] = '001005'

    r = requests.get(RAKUTEN_API_PATH, params=params)
    return JsonResponse(r.json())
