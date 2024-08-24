from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allows object owners to edit or delete. Read-only for others.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdmin(permissions.BasePermission):
    """
    Allows admin users to delete posts.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        return False
