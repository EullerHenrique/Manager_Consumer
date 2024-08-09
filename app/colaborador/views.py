from django.shortcuts import render
from django.http import HttpResponse

import app.colaborador.service.external.dto.colaborador.colaboradorDtoExternalService as colaboradorDtoExternalService
import app.colaborador.service.internal.util.relatorio.relatorioUtilService as relatorioUtilService
   
def exibirPaginaBuscarColaboradores(request):
    return render(request, 'colaborador/buscarColaboradores.html')
def exibirPaginaListarColaboradores(request, data):
    return render(request, 'colaborador/listarColaboradores.html', {'colaboradores': data})


def listarColaboradores(request):
    try:
        request.session['tokenJwt'] = request.POST.get('tokenJwt', '').replace('"', '')
        data = colaboradorDtoExternalService.listarColaboradores(request)
        exibirPaginaListarColaboradores(request, data)
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