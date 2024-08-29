from django.contrib import admin
from .models import Clientes, Producto, Marca, Medida, Categoria
# Register your models here.
admin.site.register(Clientes)
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Medida)
admin.site.register(Categoria)