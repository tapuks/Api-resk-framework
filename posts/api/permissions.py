from rest_framework.permissions import BasePermission

# CREAMOS UN PERMISO PARA QUE SOLO PUEDAN LEER LOS NO LOGEADOS Y EL ADMIN PUEDA MODIFICAR, BORRAR...
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
