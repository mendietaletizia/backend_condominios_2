from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.serializer_login import LoginSerializer

from usuarios_unidades.serializers.serializer_usuario import UsuarioSerializer
from autenticacion_seguridad.models import CustomUser
from rest_framework import permissions
from django.contrib.auth.hashers import make_password


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data.copy()
        # Solo username, password, email, role
        required_fields = ["username", "password", "email", "role"]
        for field in required_fields:
            if field not in data:
                return Response({"error": f"Falta el campo {field}"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user_id": user.id, "username": user.username, "role": user.role, "email": user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
