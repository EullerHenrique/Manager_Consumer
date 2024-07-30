from apps.colaborador.service.external.util.http.httpServiceUtil import requestGet


def listarColaboradores(tokenJwt):
    try:
        return requestGet('https://api-portal-dev.arlepton.com/ms-usuario/v1/usuarios/listar', tokenJwt)
    except Exception as e:
        raise e

