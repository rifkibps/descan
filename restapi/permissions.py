from rest_framework import permissions

class DeveloperPermission(permissions.BasePermission):

    methods_ = ("GET", "POST")

    def has_permission(self, request, view):
        print('Hello World')
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if 'Developer' in list(request.user.groups.values_list('name', flat=True)):
            return True

        if request.user.is_staff and request.method not in self.methods_:
            return True

        return False