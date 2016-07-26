
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cat',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_filter = ('nombre',)
    list_display = ('categoria',)





