from core.models import MyBook, BookInfo

from rest_framework import serializers


class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInfo


class MyBookSerializer(serializers.ModelSerializer):
    bookinfo = BookInfoSerializer(source='book_info', read_only=True)

    class Meta:
        model = MyBook
