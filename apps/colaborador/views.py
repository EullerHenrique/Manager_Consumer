import requests
import io

from django.shortcuts import render
from django.http import HttpResponse

def colaborador(request):
  return render(request, 'index.html')
   
def buscar(request):
    return render(request, 'buscarColaboradores.html')
   
def listar(request):
    tokenjwt = request.POST.get('tokenJwt')
    return obterColaboradores(tokenjwt)
     
def gerarExcel(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    colaboradores = response.json()

    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()

    # Write Headers
    headers = ["ID", "Name", "Username", "Email", "Phone"]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write Data (Starting from Row 1)
    for row, colaborador in enumerate(colaboradores, start=1):
        worksheet.write(row, 0, colaborador['id'])
        worksheet.write(row, 1, colaborador['name'])
        worksheet.write(row, 2, colaborador['username'])
        worksheet.write(row, 3, colaborador['email'])
        worksheet.write(row, 4, colaborador['phone'])

    workbook.close()
    buffer.seek(0)

    # Set up the Http response.
    filename = "django_simple.xlsx"
    response = HttpResponse(
        buffer,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=%s" % filename

    return response


def obterColaboradores(tokenjwt):
    headers = {
        'Authorization': f'Bearer {tokenjwt}',
        'Referer' : 'portal-phoenix-dev.arlepton.com'
    }
    
    response = requests.get('https://api-portal-dev.arlepton.com/ms-usuario/v1/usuarios/listar', headers=headers)
    if response.status_code != 200:
        if response.status_code == 401:
            return HttpResponse(f'Status: {response.status_code} - Sem Autorização')
        else: 
            return HttpResponse(f'Status: {response.status_code} - Erro ao buscar colaboradores')
    else:
        json = response.json()
        
        status = json.get('status')
        erro = json.get('error')
        message = json.get('message')
        data = json.get('data')

        if status != 200:
            return HttpResponse(f'Status: {status} - Erro: {erro} - Mensagem: {message}')
        else:
            return data