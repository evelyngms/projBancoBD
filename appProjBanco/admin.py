from django.contrib import admin
from .models import ContaCorrente, Historico
# Register your models here.

@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_display = ('nome_titular', 'numero_conta', 'saldo')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'tipo', 'valor', 'data_hora')
