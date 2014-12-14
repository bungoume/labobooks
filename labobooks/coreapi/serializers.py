from core.models import MyBook, BookInfo

from rest_framework import serializers


class MyBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyBook
        # fields = ('url', 'username', 'email', 'groups')


class BookInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInfo
