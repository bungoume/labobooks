# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='sales_date',
            field=models.DateField(null=True, verbose_name='発売日'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybook',
            name='book_expire_at',
            field=models.DateField(null=True, verbose_name='本の賞味期限'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybook',
            name='buy_date',
            field=models.DateField(null=True, verbose_name='購入日'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybook',
            name='buy_user',
            field=models.CharField(verbose_name='購入希望者', max_length=191, blank=True),
            preserve_default=True,
        ),
    ]
