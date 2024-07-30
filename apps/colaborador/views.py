import requests
import io
import xlsxwriter

from django.shortcuts import render
from django.http import HttpResponse

from apps.colaborador.service.external.dto.colaborador.colaboradorDtoExternalService import *

def colaborador(request):
  return render(request, 'index.html')
   
def buscar(request):
    return render(request, 'buscarColaboradores.html')
   
def listar(request):
    try:
        request.session['tokenJwt'] = request.POST.get('tokenJwt')
        data = listarColaboradores(request)
        return render(request, 'listarColaboradores.html', {'colaboradores': data})
    except Exception as e:
        return HttpResponse(e)

def gerarExcel(request):
    try:
       #Retorna um arquivo excel de exemplo
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Nome')
        worksheet.write('B1', 'Email')
        worksheet.write('C1', 'Telefone')
        row = 1
       
        worksheet.write(row, 0, 'teste')
        worksheet.write(row, 1, 'teste')
        worksheet.write(row, 2, 'teste')

        workbook.close()
        output.seek(0)
        response = HttpResponse(output, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=colaboradores.xlsx'
        return response
    except Exception as e:
        return HttpResponse(e)
        