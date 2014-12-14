# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=20, unique=True, verbose_name='ISBN')),
                ('title', models.CharField(max_length=191, verbose_name='タイトル')),
                ('title_kana', models.CharField(max_length=191, blank=True, verbose_name='タイトル(カナ)')),
                ('sub_title', models.CharField(max_length=191, blank=True, verbose_name='サブタイトル')),
                ('sub_title_kana', models.CharField(max_length=191, blank=True, verbose_name='サブタイトル(カナ)')),
                ('series_name', models.CharField(max_length=191, blank=True, verbose_name='シリーズ名')),
                ('series_name_kana', models.CharField(max_length=191, blank=True, verbose_name='シリーズ名(カナ)')),
                ('author', models.CharField(max_length=191, blank=True, verbose_name='著者')),
                ('author_kana', models.CharField(max_length=191, blank=True, verbose_name='著者(カナ)')),
                ('publisher_name', models.CharField(max_length=191, blank=True, verbose_name='出版社')),
                ('book_size', models.CharField(max_length=191, blank=True, verbose_name='本サイズ')),
                ('item_caption', models.TextField(blank=True, verbose_name='キャプション')),
                ('sales_date', models.DateField(blank=True, verbose_name='発売日')),
                ('item_price', models.IntegerField(blank=True, verbose_name='価格')),
                ('image_url', models.URLField(blank=True, verbose_name='画像URL')),
                ('genre_id', models.CharField(max_length=191, blank=True, verbose_name='書籍ジャンル')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('buy_date', models.DateField(blank=True, verbose_name='購入日')),
                ('buy_user', models.CharField(max_length=191, verbose_name='購入希望者')),
                ('manager', models.CharField(max_length=191, verbose_name='管理責任者')),
                ('buy_at', models.CharField(max_length=191, blank=True, verbose_name='購入場所')),
                ('purpose', models.TextField(blank=True, verbose_name='購入目的')),
                ('money_source', models.CharField(max_length=191, blank=True, verbose_name='資金源')),
                ('book_expire_at', models.DateField(blank=True, verbose_name='本の賞味期限')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_info', models.ForeignKey(to='core.BookInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
