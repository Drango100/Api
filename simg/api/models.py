from django.db import models

# Create your models here.

class Clientes(models.Model):
    cod_cliente=models.CharField(max_length=4)
    empre_cliente=models.CharField(max_length=100)
    nombre_cliente=models.CharField(max_length=50)
    apellido_cliente=models.CharField(max_length=50)
    dir_cliente=models.CharField(max_length=50)
    tel_cliente=models.CharField(max_length=50)

class Producto(models.Model):
    nombre_producto= models.CharField(max_length=100)
    can_maxima = models.DecimalField(max_digits=10, decimal_places=2)
    can_minima = models.DecimalField(max_digits=10, decimal_places=2)
    valor_producto = models.DecimalField(max_digits=10, decimal_places=2)
    iva_producto= models.CharField(max_length=50)
    descu_producto= models.CharField(max_length=50)
    ubi_producto= models.CharField(max_length=4)
    def _str_(self):
        return self.nombre_producto

class Marca(models.Model):
    nombre_marca= models.CharField(max_length=100)
   
    def _str_(self):
        return self.nombre_marca

class Medida(models.Model):
    descr_medida= models.CharField(max_length=200)
   
    def _str_(self):
        return self.descr_medida

class Categoria(models.Model):
    nombre_categoria= models.CharField(max_length=100)
   
    def _str_(self):
        return self.nombre_categoria