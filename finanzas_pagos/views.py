from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Gasto
from .serializers.serializer_gasto import GastoSerializer

class GastoListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'role') and user.role == 'administrador':
            return Gasto.objects.all()
        elif hasattr(user, 'role') and user.role == 'residente':
            return Gasto.objects.filter(usuario=user)
        # Otros roles pueden tener filtros personalizados
        return Gasto.objects.none()
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

class GastoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]
