import requests
from django.shortcuts import render
from django.http import HttpResponse

import apps.colaborador.service.external.dto.colaborador.colaboradorDtoExternalService as colaboradorDtoExternalService
import apps.colaborador.service.internal.util.relatorio.relatorioUtilService as relatorioUtilService

def exibirPaginaIndex(request):
    return render(request, 'index.html')
   
def exibirPaginaBuscarColaboradores(request):
    return render(request, 'buscarColaboradores.html')
   
def listarColaboradores(request):
    try:
        request.session['tokenJwt'] = request.POST.get('tokenJwt', '').replace('"', '')
        data = colaboradorDtoExternalService.listarColaboradores(request)
        return render(request, 'listarColaboradores.html', {'colaboradores': data})
    except Exception as e:
        return HttpResponse(e)

def gerarExcel(request):
    try:
        data = colaboradorDtoExternalService.listarColaboradores(request)
        byte = relatorioUtilService.gerarExcel(data, ['matricula', 'nome', 'email', 'userName', 'ufTrabalho', 'tipoApuracao', 'tipoVinculo', 'codigoArea', 'codigoEquipe', 'codigoEmpresa'])
    
        response = HttpResponse(byte, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=colaboradores.xlsx'
        return response
    except Exception as e:
        return HttpResponse(e)    