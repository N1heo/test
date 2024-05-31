from rest_framework.permissions import IsAdminUser, BasePermission


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsSuperUserOrPostOnly(BasePermission):
    """
    Custom permission to allow superusers all actions, regular users can only create (POST).
    """
    def has_permission(self, request, view):
        # Allow superusers all actions
        if request.user and request.user.is_superuser:
            return True
        # Allow regular users to only POST
        if request.method == 'POST':
            return True
        return False


class AllowPostForAll(BasePermission):
    """
    Custom permission to allow anyone to create (POST) objects,
    and only superusers to perform other actions.
    """
    def has_permission(self, request, view):
        # Allow any user (authenticated or not) to POST
        if request.method == 'POST':
            return True
        # Allow superusers any action
        if request.user and request.user.is_superuser:
            return True
        return False