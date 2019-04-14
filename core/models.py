from django.db import models

# Create your models here.

class Cesta(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cerveja(models.Model):
    id = models.AutoField(primary_key=True)
    estabelecimento = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    volume = models.FloatField()

    def __str__(self):
        return self.marca

class Estabelecimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    volume = models.FloatField()

    def __str__(self):
        return self.descricao
