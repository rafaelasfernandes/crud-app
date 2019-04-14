from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Cesta, Cerveja, Estabelecimento, Marca, Tipo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CestaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cesta
        fields = ('id', 'nome', 'data')

class CervejaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cerveja
        fields = ('id', 'estabelecimento', 'marca', 'tipo', 'valor')

class EstabelecimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('id', 'nome')

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nome')

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'descricao', 'volume')
