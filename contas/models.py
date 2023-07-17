from django.db import models

class Contas(models.Model):
    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    Nome_conta = models.CharField(max_length=65)
    vencimento = models.CharField(max_length=65)
    status = models.CharField(max_length=65, default='')
    valor = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.Nome_conta
