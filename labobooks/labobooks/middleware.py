from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.cache import add_never_cache_headers


class SecurityMiddleware(object):
    """SECURE_SSL_REDIRECTがTrueであればhttpsサイトにリダイレクトする。heroku用に作成
    """

    def process_request(self, request):
        if any([request.is_secure(), request.META.get("HTTP_X_FORWARDED_PROTO", "") == 'https']):
            return None
        elif settings.SECURE_SSL_REDIRECT:
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return HttpResponseRedirect(secure_url)


class DisableClientSideCachingMiddleware(object):
    """キャッシュを残さないよう、ヘッダにCache-Control:max-age=0を追加
    """

    def process_response(self, request, response):
        add_never_cache_headers(response)
        return response
