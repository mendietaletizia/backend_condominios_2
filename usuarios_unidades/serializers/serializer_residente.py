from rest_framework import serializers
from usuarios_unidades.models import Residente  # Ajusta el import según tu app

class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = ['id', 'nombre', 'ci', 'telefono', 'email', 'unidad_id']
