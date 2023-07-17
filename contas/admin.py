from django.contrib import admin
from contas.models import Contas

@admin.register(Contas)
class ContasAdmin(admin.ModelAdmin):
    list_display = 'Nome_conta', 'vencimento', 'status', 'valor',  
    ordering = '-id', 
