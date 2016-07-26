from django.conf.urls import url, include
from rest_framework import routers
from .views import CategoriaViewSet, ProductoViewSet


listar_producto = ProductoViewSet.as_view({
    'get': 'listar',
    'post': 'crear'
})
detalle_producto = ProductoViewSet.as_view({
    'get': 'traer',
    'put': 'actualizar',
    'patch': 'actualizado_parcial',
    'delete': 'eliminar'
})

router = routers.DefaultRouter()
router.register(r'Categoria', CategoriaViewSet)
router.register(r'Producto', ProductoViewSet)


urlpatterns = [
    url(r'^inventario/$', listar_producto, name='listar_producto'),
    url(r'^detalle_inventario/(?P<pk>[0-9]+)/$', detalle_producto, name='detalle_producto'),
    url(r'^', include(router.urls)),
]