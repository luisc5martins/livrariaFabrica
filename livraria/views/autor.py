from django.db import models
from rest_framework.viewsets import ModelViewSet


class Autor(ModelViewSet):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"
