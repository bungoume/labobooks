from core.models import MyBook, BookInfo

from rest_framework import serializers


class BookInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BookInfo


class MyBookSerializer(serializers.HyperlinkedModelSerializer):
    book_info = BookInfoSerializer('book_info')

    class Meta:
        model = MyBook
        # fields = ('url', 'username', 'email', 'groups')
