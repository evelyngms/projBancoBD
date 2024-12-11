from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_conta, name='criar_conta'),
    path('consulta/<str:numero_conta>/', views.consultar_saldo, name='consulta_conta'),
    path('depositar/<str:numero_conta>/', views.depositar, name='depositar'),
    path('sacar/<str:numero_conta>/', views.sacar, name='sacar'),
    path('encerrar/<str:numero_conta>/', views.encerrar_conta, name='encerrar_conta'),
]
