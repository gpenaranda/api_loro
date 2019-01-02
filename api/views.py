# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# ViewSets
from rest_framework import viewsets

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework import renderers

# Serializers
from api.serializers import TiposMonedaSerializer
from api.serializers import TiposClienteSerializer
from api.serializers import TiposDocumentoSerializer
from api.serializers import SumaSerializer
from api.serializers import EstatusSerializer


# Models
#from django.contrib.auth.models import User
from api.models import TiposCliente
from api.models import TiposDocumento
from api.models import Estatus
from api.models import TiposMoneda


# Custom permissions
#from api.permissions import IsOwnerOrReadOnly


class Suma(APIView):
    """
    Se realiza una suma 
    """
    
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        data= request.data
        results = SumaSerializer(data).data

        

        total = results.get('numeroUno') + results.get('numeroDos')
        
        # Creando el Arreglo en Python
        response = {}
        response['total'] = total

        return Response(response)

# Estatus Endpoint - ViewSet
class EstatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet para los estatus
    """
    queryset = Estatus.objects.all()
    serializer_class = EstatusSerializer
    permission_classes = (permissions.IsAdminUser,)


# Tipos de Cliente Endpoint - ViewSet
class TiposClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el tipo cliente  
    """
    queryset = TiposCliente.objects.all()
    serializer_class = TiposClienteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Tipos de Documento Endpoint - ViewSet
class TiposDocumentoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    
    queryset = TiposDocumento.objects.all()
    serializer_class = TiposDocumentoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Tipos de Moneda Endpoint - ViewSet
class TiposMonedaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    
    queryset = TiposMoneda.objects.all()
    serializer_class = TiposMonedaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)