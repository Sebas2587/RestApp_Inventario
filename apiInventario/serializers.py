from rest_framework import serializers
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('codigo', 'nombre_cat', 'descripcion')

        def __init__(self):
            self.cleaned_data = None

        def clean_nombreCategoria(self):
            """Comprueba que no exista un nombre de categoria igual en la db"""
            nombrecat = self.cleaned_data['nombre categoria']
            if Categoria.objects.filter(nombre=nombrecat):
                raise serializers.ValidationError('Nombre de categoria ya existe.')
            return nombrecat

        def clean_codigo(self):
            codigocat = self.cleaned_data['codigo']
            if Categoria.objects.filter(codigo=codigocat):
                raise serializers.ValidationError('Codigo ya existe. ')
            return codigocat


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'descripcion', 'cantidad', 'estado', 'categoria')

        def __init__(self):
            self.cleaned_data = None

        def clean_codigo(self):
            codigoPro = self.cleaned_data['codigo']
            if Producto.objects.filter(codigo=codigoPro):
                raise serializers.ValidationError('Codigo de producto ya existe. ')
            return codigoPro