from django.db import models

class mini_curso(models.Model):
 nome = models.CharField(max_length=150)
def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11,default='00000000000')
    data_nascimento = models.DateTimeField()
    email = models.EmailField(max_length=150)
    endereco = models.CharField(max_length=150,null=True)
    sexo = models.CharField(max_length=150,null=True)
    curso = models.CharField(max_length=150,null=True)
    mini_curso = models.ManyToManyField(mini_curso)


    def __str__(self):
        return self.nome
