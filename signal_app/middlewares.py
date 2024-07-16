from django.core.cache import cache
from django.http import HttpResponse


class RateLimitingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        ip = request.META['REMOTE_ADDR']
        rate_limit_key = f'rate_limit_{ip}'
        request_count = cache.get(rate_limit_key, 0)
        print(request_count)
        
        if request_count >= 5:
            return HttpResponse("Too many requests.")
        
        cache.set(rate_limit_key, request_count+1, timeout=60)
        response = self.get_response(request)
        return response