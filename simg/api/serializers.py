from rest_framework import serializers
from .models import Producto, Marca, Medida, Categoria

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class MarcaSeializer(serializers.ManyRelatedField):
    class Meta:
        model= Marca
        fields = '__all__'

class MedidaSeializer(serializers.ManyRelatedField):
    class Meta:
        model= Medida
        fields = '__all__'

class CategoriaSeializer(serializers.ManyRelatedField):
    class Meta:
        model= Categoria
        fields = '__all__'