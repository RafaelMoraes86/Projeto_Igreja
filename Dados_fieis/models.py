from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fiel(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    localidade = models.CharField(max_length=100)
    data = models.DateTimeField()
    foi_a_igreja = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome
