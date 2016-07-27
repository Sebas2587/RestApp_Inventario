from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    nombre_cat = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    '''def __str__(self):
        return self.codigo, self.nombre_cat'''


class Producto(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    estado = models.BooleanField(default=False)
    actualizacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    categoria = models.ForeignKey(Categoria)

    '''def __str__(self):
        return self.codigo, self.nombre'''


