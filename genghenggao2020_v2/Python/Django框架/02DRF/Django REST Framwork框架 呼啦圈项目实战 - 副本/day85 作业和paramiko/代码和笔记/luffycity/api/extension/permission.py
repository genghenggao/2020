
from rest_framework.permissions import BasePermission


class LuffyPermission(BasePermission):
    message = {"status":False,"error":"登录成功之后才能评论"}
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user:
            return True
        return False
