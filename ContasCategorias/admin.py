from django.contrib import admin
from ContasCategorias.models import Luz, Agua, Internet, PlanoDeSaude

@admin.register(Luz)
class LuzAdmin(admin.ModelAdmin):
    list_display = 'Nome_conta', 'vencimento', 'status', 'valor',
    ordering = '-id',

@admin.register(Agua)
class AguaAdmin(admin.ModelAdmin):
    list_display = 'Nome_conta', 'vencimento', 'status', 'valor',
    ordering = '-id',

@admin.register(Internet)
class InternetAdmin(admin.ModelAdmin):
    list_display = 'Nome_conta', 'vencimento', 'status', 'valor',
    ordering = '-id',

@admin.register(PlanoDeSaude)
class PlanoDeSaudeAdmin(admin.ModelAdmin):
    list_display = 'Nome_conta', 'vencimento', 'status', 'valor',
    ordering = '-id',
