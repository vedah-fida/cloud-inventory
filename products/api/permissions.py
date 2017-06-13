from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "Permission Denied"

    def has_object_permission(self, request, view, obj):
        my_safe_method = ["PUT"]
        if request.method in my_safe_method:
            return True

        return obj.user == request.user
