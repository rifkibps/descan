from rest_framework import permissions
from rest_framework import exceptions

class DeveloperPermission():
    def __init__(self, user):
        self.user = user

    def has_permission(self):
        if self.user.is_superuser or self.user.is_staff or self.user.groups.filter(name='Developer').exists():
            return True
        else:
            raise exceptions.AuthenticationFailed(
                "Authentication credentials are not valid for the given user. Make sure the user is a developer."
            )
        
class DeveloperBasePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return DeveloperPermission(request.user).has_permission()