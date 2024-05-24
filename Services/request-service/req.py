import requests
from datetime import datetime as dt
import pytz
#   Pedro Díaz | 23-05-2024
#   llamado:
#       Función que retorna el contenido del objeto "btcars" 
#       de la url https://be.buenbit.com/api/market/tickers/
#
#       Agregamos campo timestamp al response. Formato Unix. Horario local.
#
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
        raise RuntimeError(f"Sucedió un error en tiempo de ejecución: {e}")
    finally:
        return response