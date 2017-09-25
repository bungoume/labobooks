from core.models import MyBook, BookInfo

from rest_framework import serializers


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'


class MyBookSerializer(serializers.ModelSerializer):
    book_info = BookInfoSerializer(required=False, read_only=True)

    class Meta:
        model = MyBook
        fields = '__all__'
