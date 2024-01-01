from django.db import models

# Create your models here.
class usuarioSistema(models.Model):
    nombreUsuario = models.CharField(max_length=32, blank=True, null=True)
    apellidoUsuario = models.CharField(max_length=32, blank=True, null=True)
    edadUsuario = models.CharField(max_length=8, blank=True, null=True)
    profesionUsuario = models.CharField(max_length=64, blank=True, null=True)

class dispositivoSistema(models.Model):
    nombreDispositivo = models.CharField(max_length=32, blank=True, null=True)
    codigoDispositivo = models.CharField(max_length=32, blank=True, null=True)
    fabricanteDispositivo = models.CharField(max_length=32, blank=True, null=True)
    