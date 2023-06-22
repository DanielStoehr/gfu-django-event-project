from django.contrib.auth.models import AbstractUser
from rest_framework import permissions

WHITELIST_IPS = ["127.0.0.1"]


class IsPublicOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        is_admin = request.user.is_superuser
        return request.method in permissions.SAFE_METHODS or is_admin


class WhiteListPermission(permissions.BasePermission):
    """Lasse nur IPs zu, die in der WHITELIST liegen"""

    def has_permission(self, request, view):
        remote_addr = str(request.META["REMOTE_ADDR"])
        for valid_ip in WHITELIST_IPS:
            if remote_addr.startswith(valid_ip):
                return True
        return False
