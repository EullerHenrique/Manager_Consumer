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
    headers = {'Authorization': f'Bearer {tokenjwt}'}
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    colaboradores = response.json()
    return render(request, 'listarColaboradores.html', {'colaboradores': colaboradores})
    
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