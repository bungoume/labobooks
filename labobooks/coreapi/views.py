from django.http import JsonResponse

from rest_framework import viewsets
import requests

from core.models import MyBook, BookInfo
from coreapi.serializers import MyBookSerializer, BookInfoSerializer


class MyBookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyBook.objects.all()
    serializer_class = MyBookSerializer


class BookInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


def search_bookinfo(request):
    RAKUTEN_API_PATH = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522'
    keyword = request.GET.get('keyword', '')
    if not keyword:
        return JsonResponse({})
    params = {
        'applicationId': 1057827198669500530,  # rakuten applicationId for labobooks
        'format': 'json',
        'formatVersion': 2,
        'title': keyword,
        'sort': 'sales',
        # 'elements': 'title,seriesName,author,publisherName,salesDate,mediumImageUrl,isbn',

    }
    r = requests.get(RAKUTEN_API_PATH, params=params)
    return JsonResponse(r.json())
