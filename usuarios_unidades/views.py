from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers.serializer_usuario import UsuarioSerializer
from usuarios_unidades.models import Residente
from .serializers.serializer_roles import UsuarioRoleSerializer
from .serializers.serializer_residente import ResidenteSerializer
from usuarios_unidades.models import Unidad
from .serializers.serializer_unidad import UnidadSerializer


User = get_user_model()

# CU3 – Gestión de usuarios

class UserListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'role') and user.role == 'administrador':
            return User.objects.all()
        return User.objects.filter(id=user.id)
    serializer_class = UsuarioSerializer

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer


# CU4 – Gestión de roles

class UserRoleListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioRoleSerializer

class UserRoleUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioRoleSerializer

    def update(self, request, *args, **kwargs):
        # Solo administradores pueden modificar roles
        if not hasattr(request.user, "role") or request.user.role != "administrador":
            return Response({"error": "Solo un administrador puede modificar roles."}, status=403)
        data = request.data
        role = data.get("role", "").lower()
        valid_roles = ['residente', 'administrador', 'seguridad', 'empleado']
        if role not in valid_roles:
            return Response({"error": f"Rol inválido. Debe ser uno de {valid_roles}"}, status=400)
        return super().update(request, *args, **kwargs)

# CU5 – Gestión de residentes e inquilinos

class ResidenteListCreateView(generics.ListCreateAPIView):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer

class ResidenteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer

# CU6 – Gestión de unidades habitacionales
class UnidadListCreateView(generics.ListCreateAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class UnidadRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer