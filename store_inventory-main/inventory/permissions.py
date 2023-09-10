from rest_framework import permissions


class IsStaffUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
class CanViewOwnBoxes(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True  
        return obj.creator == request.user
    
class CanDeleteOwnBox(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user