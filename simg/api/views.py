
from typing import Any
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from .models import Clientes
import json

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