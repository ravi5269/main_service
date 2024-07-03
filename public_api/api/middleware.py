from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

API_KEYS = {
    'some-public-api-key': 'user-id',
}

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        if not api_key or api_key not in API_KEYS:
            raise AuthenticationFailed('Invalid API key')
        return (None, None)
