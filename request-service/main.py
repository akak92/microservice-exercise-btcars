import os
import sys
import logging
from req import llamado
from models import BTCars, BTCarsData
from mongoengine import connect
from time import sleep

#
#   Pedro Díaz | 23-05-2024
#   Función principal que almacena resultado "btcars" en el servicio local mongo.
#   MONGO_URI y URL son variables de entorno definidas en docker-compose
#
#   Se importa función llamado(url) (importada de req.py)
#   para obtener respuesta de API externa.
#   Ejecución definida en docker-compose (command), admite ejecución cada N segundos.
#


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


mongo_uri = os.getenv('MONGO_URI')
url = os.getenv('URL')

if __name__ == "__main__":

    if len(sys.argv) != 2:
        logger.error("Demasiados argumentos. Ejecutar: python main.py <segundos>.")
        sys.exit(1)
    
    N = int(sys.argv[1])
    logger.info("Servicio que consulta precio actual de Bitcoin cada N segundos.")
    logger.info(f"Configurado para: {N} segundos.")
    while True:
        try:
            conn = connect(host=mongo_uri)
            data = llamado(url)
            if data != {}:
                btcars_data = BTCarsData(**data)
                btcars = BTCars(**btcars_data.model_dump())
                btcars.save()
                logger.info(f"Se ha añadido un elemento. {btcars.serialize}")
            else:
                logger.info(f"No hay datos. Respuesta vacía. Verifique conexión a Internet.")
            
        except Exception as e:
            raise RuntimeError(f"Algo sucedió en tiempo de ejecución. {e}")
        sleep(N)


