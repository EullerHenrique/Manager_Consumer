import requests
from django.shortcuts import render
from django.http import HttpResponse

import apps.colaborador.service.external.dto.colaborador.colaboradorDtoExternalService as colaboradorDtoExternalService
import apps.colaborador.service.internal.util.excelUtilService as excelUtilService

def exibirPaginaIndex(request):
    return render(request, 'index.html')
   
def exibirPaginaBuscarColaboradores(request):
    return render(request, 'buscarColaboradores.html')
   
def listarColaboradores(request):
    try:
        request.session['tokenJwt'] = request.POST.get('tokenJwt')
        data = colaboradorDtoExternalService.listarColaboradores(request)
        return render(request, 'listarColaboradores.html', {'colaboradores': data})
    except Exception as e:
        return HttpResponse(e)

def gerarExcel(request):
    #try:
    data = requests.get('https://jsonplaceholder.typicode.com/users')
    byte = excelUtilService.gerarExcel(data)
    
    response = HttpResponse(byte, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=colaboradores.xlsx'
    return response
    #except Exception as e:
    #    return HttpResponse(e)    