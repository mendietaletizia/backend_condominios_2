from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('residente', 'Residente'),
        ('administrador', 'Administrador'),
        ('seguridad', 'Seguridad'),
        ('empleado', 'Empleado'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} ({self.role})"
