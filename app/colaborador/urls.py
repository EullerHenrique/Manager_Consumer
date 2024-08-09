from django.urls import path
from app.colaborador.controller import colaboradorController as controller  
from app.colaborador.views import views as views

urlpatterns = [
    path("buscar", views.exibirPaginaBuscarColaboradores),
    path("listar", controller.listarColaboradores),
    path("gerarExcel", controller.gerarExcel),
]
