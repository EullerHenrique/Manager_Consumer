from app.colaborador.service.external.util.http.httpUtilExternalService import requestGet


def listarColaboradores(request):
    try:
        return requestGet(request, 'https://api-portal-dev.arlepton.com/ms-usuario/v1/usuarios/listar')
    except Exception as e:
        raise e

