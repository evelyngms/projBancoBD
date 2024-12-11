from django.shortcuts import render, get_object_or_404, redirect
from .models import ContaCorrente, Historico

# Create your views here.

# Função para a página inicial
def index(request):
    return render(request, 'appProjBanco/index.html')

# Criar conta
def criar_conta(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        numero_conta = request.POST['numero_conta']
        senha = request.POST['senha']
        saldo_inicial = float(request.POST['saldo_inicial'])

        if not ContaCorrente.objects.filter(numero_conta=numero_conta).exists():
            conta = ContaCorrente.objects.create(
                nome_titular=nome, numero_conta=numero_conta, senha=senha, saldo=saldo_inicial
            )
            Historico.objects.create(conta=conta, tipo='Criação de Conta', valor=saldo_inicial)
            return redirect('consulta_conta', numero_conta=conta.numero_conta)
    return render(request, 'appProjBanco/criar_conta.html')

# Consultar saldo
def consultar_saldo(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    return render(request, 'appProjBanco/consultar_saldo.html', {'conta': conta})

# Depósito
def depositar(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    if request.method == 'POST':
        valor = float(request.POST['valor'])
        conta.saldo += valor
        conta.save()
        Historico.objects.create(conta=conta, tipo='Depósito', valor=valor)
        return redirect('consulta_conta', numero_conta=conta.numero_conta)
    return render(request, 'appProjBanco/depositar.html', {'conta': conta})

# Saque
def sacar(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    if request.method == 'POST':
        valor = float(request.POST['valor'])
        if conta.saldo >= valor:
            conta.saldo -= valor
            conta.save()
            Historico.objects.create(conta=conta, tipo='Saque', valor=valor)
            return redirect('consulta_conta', numero_conta=conta.numero_conta)
        else:
            return render(request, 'appProjBanco/sacar.html', {'conta': conta, 'erro': 'Saldo insuficiente!'})
    return render(request, 'appProjBanco/sacar.html', {'conta': conta})

# Encerrar conta
def encerrar_conta(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    if request.method == 'POST' and conta.saldo == 0:
        conta.delete()
        return redirect('criar_conta')  # Redireciona para criar uma nova conta
    return render(request, 'appProjBanco/encerrar_conta.html', {'conta': conta})

