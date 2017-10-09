import datetime
from uuid import uuid4

from django.db import models
from django.conf import settings


USER_ROLES_CHOICES = (
    ('owner', 'Owner'),
    ('admin', 'Admin'),
    ('member', 'Member'),
)

MY_BOOK_OPTIONAL_STATE_CHOICES = (
    ('available', '貸出可'),
    ('reference_only', '禁帯出'),
    ('lost', '紛失'),
    ('breakage', '破損'),
    ('unpurchased', '未購入'),
)

ACTION_CHOICES = (
    ('borrow', '貸出'),
    ('return', '返却'),
    ('renewal', '延長'),
    ('purchase_request', '購入希望'),
)


class Organization(models.Model):
    name = models.CharField("組織名", max_length=191, help_text='例:後藤研究室')
    id_slug = models.CharField(
        "短縮名", max_length=191, unique=True, db_index=True,
        help_text='URLに利用されます。英数とハイフンのみ。 例:gotolab')
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='OrganizationMember',
        related_name='org_memberships',
        through_fields=('organization', 'user'),
    )

    opt_lending_period = models.IntegerField("貸出期間(日)", default=14)
    opt_max_renewal = models.IntegerField("最大延長可能回数", default=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '組織'
        verbose_name_plural = '組織'

    def __str__(self):
        return self.name


class OrganizationMember(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        choices=USER_ROLES_CHOICES,
        max_length=32,
        default='member',
    )

    # for invitation
    invite_email = models.EmailField(null=True, blank=True)
    invite_token = models.CharField(max_length=64, null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_pending(self):
        return self.user is None

    def generate_token(self):
        return uuid4().hex

    class Meta:
        verbose_name = '組織メンバー'
        verbose_name_plural = '組織メンバー'
        unique_together = (('organization', 'user'), ('organization', 'invite_email'), )

    def __str__(self):
        return "{} - {}".format(self.organization, self.user)


# 同じ本が複数あるときどうする?
class MyBook(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    book_info = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    buy_date = models.DateField("購入日", default=datetime.date.today)
    memo = models.TextField("メモ", blank=True)
    # buy_user = models.CharField("購入者", max_length=191, blank=True)
    # buy_at = models.CharField("購入場所", max_length=191, blank=True)
    # purpose = models.TextField("購入目的", blank=True)
    # price = models.IntegerField("価格", blank=True)
    # money_source = models.CharField("資金源", max_length=191, blank=True)
    # book_expire_at = models.DateField("本の賞味期限", null=True)
    optional_state = models.CharField(
        choices=MY_BOOK_OPTIONAL_STATE_CHOICES,
        max_length=32,
        default='available',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def state(self):
        if self.events:
            last_event = self.events.latest()
            if last_event.action in ['borrow', 'renewal']:
                # if today > last_event.created_at + self.organization.opt_lending_period:
                #     return 'lending_overdue'
                return 'lending'
        if self.reservations:
            return 'reserved'
        return self.optional_state


class BookInfo(models.Model):
    isbn = models.CharField("ISBN", primary_key=True, max_length=13)  # 13桁
    title = models.CharField("タイトル", max_length=191)
    sub_title = models.CharField("サブタイトル", max_length=191, blank=True)
    series_name = models.CharField("シリーズ名", max_length=191, blank=True)
    author = models.CharField("著者", max_length=191, blank=True)
    publisher = models.CharField("出版社", max_length=191, blank=True)
    book_size = models.CharField("本サイズ", max_length=191, blank=True)
    # item_caption = models.TextField("キャプション", blank=True)
    publication_date = models.DateField("刊行日", null=True)
    # item_price = models.IntegerField("価格", blank=True)
    small_image_url = models.URLField("サムネイルURL", blank=True)
    medium_image_url = models.URLField("画像URL(中)", blank=True)
    large_image_url = models.URLField("画像URL(大)", blank=True)
    # genre_id = models.CharField("書籍ジャンル", max_length=191, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '書籍情報'
        verbose_name_plural = '書籍情報'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        'Organization', on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # mybook = ...コメントの種類が(xxページが紛失、などだとmybookに紐づくべき?)
    title = models.CharField("タイトル", max_length=191)
    body = models.TextField("本文", blank=True)
    rating = models.IntegerField("評価", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'organization', 'book')


class Reservation(models.Model):
    """予約状況。貸出完了や削除ではデータごと削除
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mybook = models.ForeignKey('MyBook', on_delete=models.CASCADE, related_name='reservations')
    created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    """追記型Table
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mybook = models.ForeignKey('MyBook', on_delete=models.CASCADE, related_name='events')
    action = models.CharField(choices=ACTION_CHOICES, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'
