from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'email', 'password']
    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.pop('role', None)
        user = User.objects.create_user(
            password=password,
            role=role,
            **validated_data
        )
        user.is_active = True
        user.save()
        return user
