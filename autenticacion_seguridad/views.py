
from autenticacion_seguridad.models import CustomUser
from usuarios_unidades.serializers.serializer_usuario import UsuarioSerializer
from rest_framework import permissions
from rest_framework import generics

# Vista para que solo el administrador cree usuarios
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Solo administradores pueden crear usuarios
        if not hasattr(request.user, "role") or request.user.role != "administrador":
            return Response({"error": "Solo un administrador puede crear usuarios."}, status=403)
        data = request.data.copy()
        # Validar rol permitido
        rol_nuevo = data.get("role", "").lower()
        roles_permitidos = ["residente", "seguridad", "empleado"]
        if rol_nuevo not in roles_permitidos:
            return Response({"error": f"Solo puedes crear usuarios con roles: {roles_permitidos}."}, status=400)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user_id": user.id, "username": user.username, "role": user.role, "email": user.email}, status=201)
        return Response(serializer.errors, status=400)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.serializer_login import LoginSerializer

from usuarios_unidades.serializers.serializer_usuario import UsuarioSerializer
from autenticacion_seguridad.models import CustomUser
from rest_framework import permissions
from django.contrib.auth.hashers import make_password
from autenticacion_seguridad.models import CustomUser


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response({
                "user_id": user.id,
                "username": user.username,
                "role": getattr(user, "role", "N/A")
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        return Response({"message": "Sesión cerrada correctamente."})
