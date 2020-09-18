from rest_framework.authentication import BaseAuthentication

from api import models

class LuffyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        token = request.query_params.get('token')
        if not token:
            return (None,None)

        user_object = models.UserInfo.objects.filter(token=token).first()
        if user_object:
            return (user_object,token)
        return (None,None)
