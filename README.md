# Entrega 3 – Artesanías al Hierro

Sitio web realizado con Django para mostrar artículos de herrería artesanal.

## Funcionalidades

- Herencia de plantillas HTML
- Formulario para cargar:
  - Categorías
  - Artesanos
  - Artículos
- Formulario de búsqueda por título de artículo
- Administración con Django admin

## Cómo probar

1. Crear entorno virtual:  
   `python -m venv env`

2. Activar entorno virtual:  
   - En Windows: `env\Scripts\activate`
   - En Mac/Linux: `source env/bin/activate`

3. Instalar dependencias:  
   `pip install django`

4. Migrar base de datos:  
   `python manage.py migrate`

5. Crear superusuario:  
   `python manage.py createsuperuser`

6. Correr servidor:  
   `python manage.py runserver`

7. Ingresar a:  
   - Sitio web: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

