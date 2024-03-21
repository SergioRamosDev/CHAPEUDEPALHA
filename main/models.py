from django.db import models

class Beneficiario(models.Model):

    nome = models.CharField(max_length=255)
    pis = models.IntegerField()
    cpf = models.IntegerField()
    nome_pai = models.CharField(max_length=255)
    nome_mae = models.CharField(max_length=255)
    quantidade_filhos = models.IntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField(null=True)
    comprovante_de_residencia = models.IntegerField()
    numero_carteira_trabalho = models.IntegerField()

    def __str__(self):
        return self.nome

