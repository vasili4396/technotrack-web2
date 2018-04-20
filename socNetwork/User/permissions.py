from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return not request.user.is_authenticated()
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy', 'change_password']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return request.user.is_authenticated()
        elif view.action in ['update', 'partial_update', 'change_password']:
            return request.user.is_authenticated() and obj.id == request.user.id
        elif view.action == 'destroy':
            return request.user.is_authenticated() and request.user.is_staff
        else:
            return False

