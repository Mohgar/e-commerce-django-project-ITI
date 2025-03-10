from rest_framework.permissions import BasePermission



class AdminDeletePermission(BasePermission):
    message = 'only admin can delete iteams'
    def has_permission(self, request, view):
      
        if request.method == 'DELETE':
            return request.user.is_staff
        return True