from django.db import models

# Create your models here.

class Clientes(models.Model):
    cod_cliente=models.CharField(max_length=4)
    empre_cliente=models.CharField(max_length=100)
    nombre_cliente=models.CharField(max_length=50)
    apellido_cliente=models.CharField(max_length=50)
    dir_cliente=models.CharField(max_length=50)
    tel_cliente=models.CharField(max_length=50)