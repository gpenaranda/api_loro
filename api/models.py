# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Estatus
class Estatus(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ('created',)

# Tipos de Moneda
class TiposMoneda(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, default='')
    simbolo = models.CharField(max_length=1, blank=True, default='')
    
    class Meta:
        ordering = ('created',)
        db_table = 'api_tipos_moneda'  

# Tipos de Cliente
class TiposCliente(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)
        db_table = 'api_tipos_cliente'

# Tipos de Documento
class TiposDocumento(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, default='')
    codigo = models.CharField(max_length=1, blank=True, default='')
    codigo_banplus = models.CharField(max_length=3, blank=True, default='')
    
    class Meta:
        ordering = ('created',)
        db_table = 'api_tipos_documento'        

# Clientes
class Clientes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    estatus = models.CharField(max_length=1, blank=True, default='')
    tiposCliente = models.ManyToManyField(TiposCliente,db_table='api_tiposcliente_cliente')
    
    class Meta:
        ordering = ('created',)
