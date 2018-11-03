from django.apps import AppConfig
from django.conf import settings
# from amazon.api import AmazonAPI
import bottlenose


_amazon = None


def set_amazon():
    global _amazon
    if settings.AMAZON_PRODUCT_ADVERTISING_ID:
        _amazon = bottlenose.Amazon(
            settings.AMAZON_PRODUCT_ADVERTISING_ID,
            settings.AMAZON_PRODUCT_ADVERTISING_SECRET,
            settings.AMAZON_ASSOCIATE_TAG,
            Region=settings.AMAZON_ASSOCIATE_REGION,
            MaxQPS=0.9)
    else:
        _amazon = None


def get_amazon():
    return _amazon


class CoreApiConfig(AppConfig):
    name = 'coreapi'

    def ready(self):
        set_amazon()
