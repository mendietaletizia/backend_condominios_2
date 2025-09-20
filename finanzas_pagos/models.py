from django.db import models
from django.conf import settings

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    proveedor = models.CharField(max_length=255, blank=True, null=True)
    registrado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="gastos_registrados"
    )

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
