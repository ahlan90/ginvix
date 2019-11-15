from django.db import models

# Create your models here.
from rest_framework import viewsets


class Festa(models.Model):

    email_usuario = models.EmailField()

    nome = models.CharField(max_length=300)
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    url_image = models.CharField(max_length=500)
