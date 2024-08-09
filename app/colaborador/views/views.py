from django.shortcuts import render

def exibirPaginaBuscarColaboradores(request):
    return render(request, 'colaborador/buscarColaboradores.html')
def exibirPaginaListarColaboradores(request, data):
    return render(request, 'colaborador/listarColaboradores.html', {'colaboradores': data})