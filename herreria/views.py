from django.shortcuts import render, redirect
from .models import Articulo
from .forms import CategoriaForm, ArtesanoForm, ArticuloForm

def inicio(request):
    return render(request, "inicio.html")

def cargar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, "formulario.html", {"form": form, "titulo": "Cargar Categoría"})

def cargar_artesano(request):
    if request.method == 'POST':
        form = ArtesanoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ArtesanoForm()
    return render(request, "formulario.html", {"form": form, "titulo": "Cargar Artesano"})

def cargar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ArticuloForm()
    return render(request, "formulario.html", {"form": form, "titulo": "Cargar Artículo"})

def buscar_articulo(request):
    resultado = None
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        resultado = Articulo.objects.filter(titulo__icontains=titulo)
    return render(request, "buscar.html", {"resultado": resultado})
