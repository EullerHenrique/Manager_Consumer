from django.shortcuts import render

def exibirPaginaIndex(request):
    return render(request, 'index.html')
