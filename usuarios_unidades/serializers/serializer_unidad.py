from rest_framework import serializers
from usuarios_unidades.models import Unidad
from django.contrib.auth import get_user_model

User = get_user_model()

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['id', 'numero_casa', 'metros_cuadrados', 'estado', 'propietario_id']
