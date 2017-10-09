import dateutil.parser
import dripper
from dripper import ValueDripper as D


def as_int(num_str):
    try:
        num = int(float(num_str))
    except (ValueError, TypeError):
        return 0
    return num


def as_date(dt_str):
    """ 文字列の日時を受けとり、 date形式でかえす
    """
    try:
        # FIXME: 月日の順序が担保されてるか注意
        dt = dateutil.parser.parse(dt_str)
    except (ValueError, TypeError):
        return None
    return dt.date().isoformat()


def list_to_str(list_or_str):
    """ list形式はカンマ繋ぎにしてstrで返す
    """
    if isinstance(list_or_str, list):
        try:
            return ', '.join(list_or_str)
        except:
            pass
    return list_or_str


amazon_dripper_declaration = {
    "items": {
        "__type__": "list",
        "__source_root__": ("ItemSearchResponse", "Items", "Item"),
        "title": D(("ItemAttributes", "Title"), default=""),
        "isbn": D(("ItemAttributes", "EAN"), default=""),
        "small_image_url": D(("SmallImage", "URL"), default=""),
        "medium_image_url": D(("MediumImage", "URL"), default=""),
        "large_image_url": D(("LargeImage", "URL"), default=""),
        "publication_date": D(
            ("ItemAttributes", "PublicationDate"), converter=as_date, default=None),
        "publisher": D(("ItemAttributes", "Publisher"), default=""),
        "book_size": D(("ItemAttributes", "Binding"), default=""),
        "author": D(("ItemAttributes", "Author"), converter=list_to_str, default=""),
        "amazon_url": D("DetailPageURL", default=None),
    },
    "total": D(("ItemSearchResponse", "Items", "TotalResults"), converter=as_int, default=0),
}
amazon_dripper = dripper.dripper_factory(amazon_dripper_declaration)


openbd_dripper_declaration = {
    "items": {
        "__type__": "list",
        # "__source_root__": ("ItemSearchResponse", "Items", "Item"),
        "title": D(("summary", "title"), default=""),
        "isbn": D(("summary", "isbn"), default=""),
        # "small_image_url": D(("SmallImage", "URL"), default=""),
        # "medium_image_url": D(("MediumImage", "URL"), default=""),
        # "large_image_url": D(("LargeImage", "URL"), default=""),
        "publication_date": D(("summary", "pubdate"), default=""),
        "publisher": D(("summary", "publisher"), default=""),
        # "book_size": D(("ItemAttributes", "Binding"), default=""),
        "author": D(("summary", "author"), default=""),
        # "amazon_url": D("DetailPageURL", default=""),
    },
    # "total": D(("ItemSearchResponse", "Items", "TotalResults"), converter=as_int, default=0),
}
openbd_dripper = dripper.dripper_factory(openbd_dripper_declaration)
