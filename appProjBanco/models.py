from django.db import models

class ContaCorrente(models.Model):
    nome_titular = models.CharField(max_length=100)
    numero_conta = models.CharField(max_length=10, unique=True)
    senha = models.CharField(max_length=4)
    saldo = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.nome_titular} - Conta {self.numero_conta}"

class Historico(models.Model):
    conta = models.ForeignKey(ContaCorrente, on_delete=models.CASCADE, related_name="historico")
    data_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)  # Ex: 'Depósito', 'Saque'
    valor = models.FloatField()

    def __str__(self):
        return f"{self.tipo} - R${self.valor:.2f} em {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}"
