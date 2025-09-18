from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# -------------------------------
# CU5 – Residentes e Inquilinos
# -------------------------------
class Residente(models.Model):
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    unidad = models.ForeignKey('Unidad', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.ci}"

# -------------------------------
# CU6 – Unidades Habitacionales
# -------------------------------
class Unidad(models.Model):
    ESTADOS = [
        ('propietario', 'Propietario'),
        ('alquiler', 'Alquiler'),
        ('anticretico', 'Anticrético'),
    ]

    numero_casa = models.IntegerField(unique=True)
    metros_cuadrados = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    propietario_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Unidad {self.numero_casa} - {self.estado}"
