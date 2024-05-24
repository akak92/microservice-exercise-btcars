from flask import Blueprint, request
import os
from api.models import BTCars
btcars_bp = Blueprint('btcars_bp', __name__)

#
#   Pedro Diaz - 23-05-2024
#   
#    Endpoints para resolver ejercicio. Utilizamos clase BTCars definida en models.py
#    Formato utilizado de timestamp: Epoch int
#    
#   GET_BTCars(timestamp)   
#       decorador => /btcars/<int:timestamp>    
#       ejemplo de llamada => /btcars/1716494100
#       retorna único documento encontrado para ese timestamp.
#
#   promedio()
#       decorador => /btcars/promedio
#       ejemplo de llamada => /btcars/promedio?init=1716494100&end=1716494150
#       requiere de parámetros init y end
#       retorna el promedio de los documentos que se encuentren entre el rango establecido.
#
#   GET_BTCars_Pagination()
#       decorador => /btcars
#       ejemplo de llamada => /btcars?page=1&init=1716494100&end=1716494150
#       requiere de parámetros page, init y end
#       retorna conjunto de resultados (paginados) con o sin filtro de timestamp.

@btcars_bp.route('/btcars/<int:timestamp>', methods=['GET'])
def GET_BTCars(timestamp):
    try:
        message = ""
        data = {}
        status = 200

        btcars = BTCars.objects(timestamp=timestamp).first()
        if btcars is not None:
            message = 'Documento encontrado en MongoDB'
            data = btcars.serialize
        else:
            message = 'Documento no encontrado en MongoDB'
            status = 404
    except Exception as e:
        message = f'Ha ocurrido un error. Error: {e}'
        status = 500
    finally:
        response = {
            'message' : message,
            'data' : data,
        }, status
        return response

@btcars_bp.route('/btcars/promedio', methods=['GET'])
def promedio():
    try:
        init = int(request.args.get('init')) if request.args.get('init') else None
        end = int(request.args.get('end')) if request.args.get('end') else None

        message = ""
        prom = 0
        status = 200

        if init is not None and end is not None:
            if init > end:
                message = "Búsqueda mal formada. end debe ser mayor que init."
                status = 400
                prom = None
            else:
                btcars = BTCars.objects(timestamp__gte=init, timestamp__lte=end)
                if btcars is not None:
                    prom = btcars.average('purchase_price')
                    message = "Promedio obtenido exitosamente."
                    status = 200
                else:
                    message = "No existen documentos para el rango solicitado."
                    status = 404
                    prom = None
        else:
            message = "Consulta mal formada. Se requieren parametros init Y end"
            status = 400
            prom = None

    except Exception as e:
        message = f'Ha ocurrido un error. Error: {e}'
        status = 500
    finally:
        response = {
            'message' : message,
            'prom' : prom,
            'elements' : [btcars.serialize for btcars in btcars] if btcars else None
        }, status
        return response
    
@btcars_bp.route('/btcars', methods=['GET'])
def GET_BTCars_pagination():
    try:
        message = ""
        status = 200
        init = int(request.args.get('init')) if request.args.get('init') else None
        end = int(request.args.get('end')) if request.args.get('end') else None
        page = int(request.args.get('page')) if request.args.get('page') else None

        DEFAULT_PAGE_SIZE = int(os.getenv('DEFAULT_PAGE_SIZE'))
        index = (page - 1) * DEFAULT_PAGE_SIZE

        if page is not None:
            if page >= 1:
                if init is not None and end is not None:
                    btcars = BTCars.objects(timestamp__gte=init, timestamp__lte=end).skip(index).limit(DEFAULT_PAGE_SIZE)
                    elements = [btcars.serialize for btcars in btcars]
                    message = "Documentos obtenidos con filtro de timestamp."
                    status = 200
                else:
                    if init is None and end is None:
                        btcars = BTCars.objects.skip(index).limit(DEFAULT_PAGE_SIZE)
                        elements = [btcars.serialize for btcars in btcars]
                        message = "Documentos obtenidos sin filtro de timestamp."
                        status = 200
                    else:
                        message = "Query mal formada. Se necesitan parámetros init Y end."
                        status = 400
                        elements = None
            else:
                message = "La página no puede ser menor que 1"
                status = 400
                elements = None
        else:
            message = "Se necesita parámetro page para paginación"
            elements = None
            status = 400
    except Exception as e:
        message = f"ha ocurrido un error. {e}"
        elements = None
        status = 500
    finally:
        response = {
            'message' : message,
            'elements' : elements
        }, status
        return response