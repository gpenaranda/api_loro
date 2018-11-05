from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import TiposCliente, TiposDocumento, Estatus

class EstatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Estatus
        fields = ('nombre', 'id')

class TiposClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TiposCliente
        fields = ('nombre', 'id')

class TiposDocumentoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TiposDocumento
        fields = ('nombre', 'id','codigo','codigo_banplus')

class SumaSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   numeroUno = serializers.IntegerField()
   numeroDos = serializers.IntegerField()

