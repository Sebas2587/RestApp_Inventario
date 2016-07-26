from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer
from.models import Producto, Categoria


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
