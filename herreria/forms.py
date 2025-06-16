from django import forms
from .models import Categoria, Artesano, Articulo

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ArtesanoForm(forms.ModelForm):
    class Meta:
        model = Artesano
        fields = ['nombre', 'especialidad', 'contacto']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'descripcion', 'categoria', 'artesano']
