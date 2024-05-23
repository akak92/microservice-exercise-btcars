import requests

#   Pedro Díaz | 23-05-2024
#   llamado:
#       Función que retorna el contenido del objeto "btcars" 
#       de la url https://be.buenbit.com/api/market/tickers/
#

def llamado(URL):
    try:
        response = {}
        resp = requests.get(URL)
        if resp.status_code == 200:
            data = resp.json()
            response = data['object']['btcars']
    except Exception as e:
        raise ConnectionError(f"Falló la conexión a la URL solicitada: {str(e)}")
    finally:
        return response