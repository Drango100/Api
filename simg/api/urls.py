from django.urls import path
from .views import ProductoView, ClientesView

urlpatterns = [
    path('clientes/', ClientesView.as_view(), name='clientes_list'),
    path('clientes/<int:id>/', ClientesView.as_view(), name='clientes_detail'),
    path('productos/', ProductoView.as_view(), name='productos_list'),
    path('productos/<int:id>/', ProductoView.as_view(), name='productos_detail'),
]