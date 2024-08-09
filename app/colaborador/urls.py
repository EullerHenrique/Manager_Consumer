from django.urls import path
from app.colaborador import views

urlpatterns = [
    path("buscar", views.exibirPaginaBuscarColaboradores),
    path("listar", views.listarColaboradores),
    path("gerarExcel", views.gerarExcel),
]
