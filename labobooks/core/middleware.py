from django.utils.cache import patch_cache_control, patch_response_headers
from django.utils.deprecation import MiddlewareMixin


class DisableClientSideCachingMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        patch_response_headers(response, cache_timeout=-1)
        patch_cache_control(response, no_cache=True, private=True)
        return response
