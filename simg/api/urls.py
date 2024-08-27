from django.urls import path
from .views import ClientesView

urlpatterns =[
    path('cliente/', ClientesView.as_view(), name= 'clientes list'),
    path('cliente/<int:id>', ClientesView.as_view(), name= 'clientes_process')
]