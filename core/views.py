from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Cesta, Cerveja, Estabelecimento, Marca, Tipo
from core.serializers import UserSerializer, GroupSerializer, CestaSerializer, CervejaSerializer, EstabelecimentoSerializer, MarcaSerializer, TipoSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CestaViewSet(viewsets.ModelViewSet):
    queryset = Cesta.objects.all()
    serializer_class = CestaSerializer

class CervejaViewSet(viewsets.ModelViewSet):
    queryset = Cerveja.objects.all()
    serializer_class = CervejaSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
