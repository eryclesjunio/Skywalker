from django.contrib.auth.models import User as Superuser
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=1200)
    siap = models.IntegerField()
    matriculado = models.BooleanField(default=False)
    categoria = models.CharField(max_length=50, default='Indefinida')
    nivel = models.IntegerField()

    def __str__(self):
        return self.username
    
class Turma(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, default='Indefinida')
    responsavel = models.ForeignKey(Superuser, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo

class Matricula(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)






    
