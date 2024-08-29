
from typing import Any
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from .models import Clientes, Producto, Marca, Medida, Categoria
import json

#clase cliente
class ClientesView(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request,id=0):
        if(id>0):
            clientes_list=list(Clientes.objects.filter(id=id).values())
            if len(clientes_list) > 0:
                Cliente=clientes_list[0]
                datos = {'message': "success", 'cliente': Cliente}
            else:
                datos = {'message': "clientes no encontrados"}
            return JsonResponse(datos)
        else:
            clientes_list = list(Clientes.objects.values())  
        if len(clientes_list) > 0:  
            datos = {'message': "success", 'cliente': clientes_list}
        else:
            datos = {'message': "clientes no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Clientes.objects.create(
            cod_cliente=jd['cod_cliente'],
            empre_cliente=jd['empre_cliente'],
            nombre_cliente=jd['nombre_cliente'], 
            apellido_cliente=jd['apellido_cliente'],
            dir_cliente=jd['dir_cliente'],
            tel_cliente=jd['tel_cliente']
            )
        datos = {'message': "success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        # Decodificar el cuerpo de la solicitud
        jd = json.loads(request.body)
        
        try:
            cliente = Clientes.objects.get(id=id)
            
            cliente.cod_cliente = jd.get('cod_cliente', cliente.cod_cliente)
            cliente.apellido_cliente = jd.get('apellido_cliente', cliente.apellido_cliente)
            cliente.empre_cliente = jd.get('empre_cliente', cliente.empre_cliente)
            cliente.nombre_cliente = jd.get('nombre_cliente', cliente.nombre_cliente)
            cliente.dir_cliente = jd.get('dir_cliente', cliente.dir_cliente)
            cliente.tel_cliente = jd.get('tel_cliente', cliente.tel_cliente)
            
            cliente.save()
            
            datos = {'message': "success"}
        except Clientes.DoesNotExist:
            datos = {'message': "cliente no encontrado"}
        
        return JsonResponse(datos)
    
    def delete(self, request,id):
        clientes_list=list(Clientes.objects.filter(id=id).values())
        if len(clientes_list) > 0:
            Clientes.objects.filter(id=id).delete()
            datos = {'message': "success"}
        
        else:
            datos = {'message': "cliente no encontrado"}
        return JsonResponse(datos)

#clase producto

class ProductoView(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request,id=0):
        if(id>0):
            Producto_list=list(Producto.objects.filter(id=id).values())
            if len(Producto_list) > 0:
                Producto=Producto_list[0]
                datos = {'message': "success", 'cliente': Producto}
            else:
                datos = {'message': "clientes no encontrados"}
            return JsonResponse(datos)
        else:
            Producto_list = list(Producto.objects.values())  
        if len(Producto_list) > 0:  
            datos = {'message': "success", 'Producto': Producto_list}
        else:
            datos = {'message': "clientes no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Producto.objects.create(
            nombre_producto=jd['nombre_producto'],
            can_maxima=jd['can_maxima'],
            can_minima=jd['can_minima'], 
            valor_producto=jd['valor_producto'],
            iva_producto=jd['iva_producto'],
            descu_producto=jd['descu_producto'],
            ubi_producto=jd['ubi_producto']
            )
        datos = {'message': "success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        # Decodificar el cuerpo de la solicitud
        jd = json.loads(request.body)
        
        try:
            producto = Producto.objects.get(id=id)
            
            producto.nombre_producto = jd.get('nombre_producto', producto.nombre_producto)
            producto.can_maxima = jd.get('can_maxima', producto.can_maxima)
            producto.can_minima = jd.get('can_minima', producto.can_minima)
            producto.valor_producto = jd.get('valor_producto', producto.valor_producto)
            producto.iva_producto = jd.get('iva_producto', producto.iva_producto)
            producto.descu_producto = jd.get('descu_producto', producto.descu_producto)
            
            producto.save()
            
            datos = {'message': "success"}
        except Producto.DoesNotExist:
            datos = {'message': "Producto no encontrado"}
        
        return JsonResponse(datos)
    
    def delete(self, request,id):
        Producto_list=list(Producto.objects.filter(id=id).values())
        if len(Producto_list) > 0:
            Producto.objects.filter(id=id).delete()
            datos = {'message': "success"}
        
        else:
            datos = {'message': "Producto no encontrado"}
        return JsonResponse(datos)

#clase marca

class MarcaView(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request,id=0):
        if(id>0):
            Marca_list=list(Producto.objects.filter(id=id).values())
            if len(Marca_list) > 0:
                Marca=Marca_list[0]
                datos = {'message': "success", 'cliente': Marca}
            else:
                datos = {'message': "Marca no encontrada"}
            return JsonResponse(datos)
        else:
            Marca_list = list(Marca.objects.values())  
        if len(Marca_list) > 0:  
            datos = {'message': "success", 'Marca': Marca_list}
        else:
            datos = {'message': "Marca no encontrada"}
        return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Marca.objects.create(
            nombre_marca=jd['nombre_marca'],
            
            )
        datos = {'message': "success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        # Decodificar el cuerpo de la solicitud
        jd = json.loads(request.body)
        
        try:
            marca = Marca.objects.get(id=id)
            
            marca.nombre_marca = jd.get('nombre_marca', marca.nombre_marca)
            
            marca.save()
            
            datos = {'message': "success"}
        except Producto.DoesNotExist:
            datos = {'message': "Marca no encontada"}
        
        return JsonResponse(datos)
    
    def delete(self, request,id):
        MarcMarca_list=list(Marca.objects.filter(id=id).values())
        if len(MarcMarca_list) > 0:
            Producto.objects.filter(id=id).delete()
            datos = {'message': "success"}
        
        else:
            datos = {'message': "Marca no encontrada"}
        return JsonResponse(datos)



#clase medida

class MedidaView(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request,id=0):
        if(id>0):
            Medida_list=list(Medida.objects.filter(id=id).values())
            if len(Medida_list) > 0:
                Medida=Medida_list[0]
                datos = {'message': "success", 'Medidas': Medida}
            else:
                datos = {'message': "Medidas no encontradas"}
            return JsonResponse(datos)
        else:
            Medida_list = list(Marca.objects.values())  
        if len(Medida_list) > 0:  
            datos = {'message': "success", 'Medidas': Medida_list}
        else:
            datos = {'message': "Medida no encontrada"}
        return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Medida.objects.create(
            descr_medida=jd['descr_medida'],
            
            )
        datos = {'message': "success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        # Decodificar el cuerpo de la solicitud
        jd = json.loads(request.body)
        
        try:
            medida = Medida.objects.get(id=id)
            
            medida.descr_medida = jd.get('descr_medida', medida.descr_medida)
            
            medida.save()
            
            datos = {'message': "success"}
        except Medida.DoesNotExist:
            datos = {'message': "Medidas no encontada"}
        
        return JsonResponse(datos)
    
    def delete(self, request,id):
        Medida_list=list(Marca.objects.filter(id=id).values())
        if len(Medida_list) > 0:
            Medida.objects.filter(id=id).delete()
            datos = {'message': "success"}
        
        else:
            datos = {'message': "Medidas no encontradas"}
        return JsonResponse(datos)

#clase categoria

class CategoriaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            categoria_list = list(Categoria.objects.filter(id=id).values())
            if len(categoria_list) > 0:
                categoria = categoria_list[0]
                datos = {'message': "success", 'Categoria': categoria}
            else:
                datos = {'message': "Categoria no encontrada"}
        else:
            categoria_list = list(Categoria.objects.values())
            if len(categoria_list) > 0:
                datos = {'message': "success", 'Categorias': categoria_list}
            else:
                datos = {'message': "Categorias no encontradas"}
        return JsonResponse(datos)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            Categoria.objects.create(
                nombre_categoria=jd['nombre_categoria'],              )
            datos = {'message': "success"}
        except KeyError as e:
            datos = {'message': f"Falta el campo {str(e)}"}
        except json.JSONDecodeError:
            datos = {'message': "Error al decodificar JSON"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        try:
            categoria = Categoria.objects.get(id=id)
            
            categoria.nombre_categoria = jd.get('nombre_categoria', categoria.nombre_categoria)  
            
            categoria.save()
            
            datos = {'message': "success"}
        
        except Categoria.DoesNotExist:
        
            datos = {'message': "Categoria no encontrada"}
        
        except json.JSONDecodeError:
        
            datos = {'message': "Error al decodificar JSON"}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        categoria_list = list(Categoria.objects.filter(id=id).values())
        if len(categoria_list) > 0:
            Categoria.objects.filter(id=id).delete()
            datos = {'message': "success"}
        else:
            datos = {'message': "Categoria no encontrada"}
        return JsonResponse(datos)
