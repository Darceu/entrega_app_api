from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    correo = models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=20)