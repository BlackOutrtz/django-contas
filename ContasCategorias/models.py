from django.db import models

class Luz(models.Model):
    class Meta:
        verbose_name = 'Luz'
        verbose_name_plural = 'Luz'
    
    Nome_conta = models.CharField(max_length=65)
    vencimento = models.CharField(max_length=65)
    status = models.CharField(max_length=65, default='')
    valor = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.Nome_conta
    
class Internet(models.Model):
    class Meta:
        verbose_name = 'Internet'
        verbose_name_plural = 'Internet'
    
    Nome_conta = models.CharField(max_length=65)
    vencimento = models.CharField(max_length=65)
    status = models.CharField(max_length=65, default='')
    valor = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.Nome_conta

class Agua(models.Model):
    class Meta:
        verbose_name = 'Agua'
        verbose_name_plural = 'Agua'
    
    Nome_conta = models.CharField(max_length=65)
    vencimento = models.CharField(max_length=65)
    status = models.CharField(max_length=65, default='')
    valor = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.Nome_conta
    
class PlanoDeSaude(models.Model):
    class Meta:
        verbose_name = 'PlanoDeSaude'
        verbose_name_plural = 'PlanoDeSaude'
    
    Nome_conta = models.CharField(max_length=65)
    vencimento = models.CharField(max_length=65)
    status = models.CharField(max_length=65, default='')
    valor = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.Nome_conta
