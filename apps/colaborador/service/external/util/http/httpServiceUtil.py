import requests

def requestGet(url, tokenjwt):
    headers = {
        'Authorization': f'Bearer {tokenjwt}',
        'Referer' : 'portal-phoenix-dev.arlepton.com'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        if response.status_code == 401:
            raise Exception(f'Status: {response.status_code} - Sem Autorização')
        else: 
            raise Exception(f'Status: {response.status_code} - Erro realizar a busca')
    else:
        json = response.json()
        
        status = json.get('status')
        erro = json.get('error')
        message = json.get('message')
        data = json.get('data')

        if status != 200:
            raise Exception(f'Status: {status} - Erro: {erro} - Mensagem: {message}')
        else:
            return data
