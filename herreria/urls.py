from django.urls import path
from .views import inicio, cargar_categoria, cargar_artesano, cargar_articulo, buscar_articulo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('categoria/', cargar_categoria, name='cargar_categoria'),
    path('artesano/', cargar_artesano, name='cargar_artesano'),
    path('articulo/', cargar_articulo, name='cargar_articulo'),
    path('buscar/', buscar_articulo, name='buscar_articulo'),
]
