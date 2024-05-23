import requests
from datetime import datetime as dt
import pytz
#   Pedro Díaz | 23-05-2024
#   llamado:
#       Función que retorna el contenido del objeto "btcars" 
#       de la url https://be.buenbit.com/api/market/tickers/
#
#       Agregamos campo timestamp al response. Formato Epoch. Horario local.

def llamado(URL):
    try:
        response = {}
        resp = requests.get(URL)
        if resp.status_code == 200:
            data = resp.json()
            response = data['object']['btcars']
            timezone_ar = pytz.timezone('America/Argentina/Buenos_Aires')
            timestamp = dt.now(timezone_ar)
            response['timestamp'] = int(timestamp.timestamp())
    except Exception as e:
        raise ConnectionError(f"Falló la conexión a la URL solicitada: {str(e)}")
    finally:
        return response