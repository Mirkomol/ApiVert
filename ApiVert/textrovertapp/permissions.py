from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to modify data.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow superusers to perform write operations.
        return request.user and request.user.is_superuser
