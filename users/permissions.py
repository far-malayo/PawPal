from rest_framework import permissions

class IsVetAdmin(permissions.BasePermission):
    """
    Custom permission to only allow vet admins to access a view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.is_vet_admin

class IsOwnerOrVetAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or vet admins to access it.
    """
    def has_object_permission(self, request, view, obj):
        # Check if user is vet admin
        if request.user.profile.is_vet_admin:
            return True
            
        # Check if the object has an owner field that matches the request user
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
            
        return False