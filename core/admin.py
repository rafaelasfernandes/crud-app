from django.contrib import admin
from .models import Cesta, Cerveja, Estabelecimento, Marca, Tipo
# Register your models here.

admin.site.register(Cesta)
admin.site.register(Cerveja)
admin.site.register(Estabelecimento)
admin.site.register(Marca)
admin.site.register(Tipo)
