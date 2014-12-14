from django.db import models

# class Library(models.Model):
#     ...


# class BookShelf(models.Model):
#     name = models.CharField("研究室名", max_length=191)


class MyBook(models.Model):
    book_info = models.ForeignKey('BookInfo')
    buy_date = models.DateField("購入日", blank=True)
    buy_user = models.CharField("購入希望者", max_length=191)
    manager = models.CharField("管理責任者", max_length=191)
    buy_at = models.CharField("購入場所", max_length=191, blank=True)
    purpose = models.TextField("購入目的", blank=True)
    money_source = models.CharField("資金源", max_length=191, blank=True)
    book_expire_at = models.DateField("本の賞味期限", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookInfo(models.Model):
    isbn = models.CharField("ISBN", unique=True, max_length=20)
    title = models.CharField("タイトル", max_length=191)
    title_kana = models.CharField("タイトル(カナ)", max_length=191, blank=True)
    sub_title = models.CharField("サブタイトル", max_length=191, blank=True)
    sub_title_kana = models.CharField("サブタイトル(カナ)", max_length=191, blank=True)
    series_name = models.CharField("シリーズ名", max_length=191, blank=True)
    series_name_kana = models.CharField("シリーズ名(カナ)", max_length=191, blank=True)
    author = models.CharField("著者", max_length=191, blank=True)
    author_kana = models.CharField("著者(カナ)", max_length=191, blank=True)
    publisher_name = models.CharField("出版社", max_length=191, blank=True)
    book_size = models.CharField("本サイズ", max_length=191, blank=True)
    item_caption = models.TextField("キャプション", blank=True)
    sales_date = models.DateField("発売日", blank=True)
    item_price = models.IntegerField("価格", blank=True)
    image_url = models.URLField("画像URL", blank=True)
    genre_id = models.CharField("書籍ジャンル", max_length=191, blank=True)
