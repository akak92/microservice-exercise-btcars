#
#   Pedro Díaz | 23-05-2023
#   Test unitarios para controlador BTCars 
#   
import os

TEST_INIT_VALUE= os.getenv('TEST_INIT_VALUE')
TEST_END_VALUE= os.getenv('TEST_END_VALUE')
TEST_TIMESTAMP= os.getenv('TEST_TIMESTAMP')
TEST_PAGE_VALUE= os.getenv('TEST_PAGE_VALUE')

#
# Pruebas unitarias para la obtención de precio bitcoin
#

def test_btcars_GET_BTCars_success(app, client):
    response = client.get(f'/btcars/{TEST_TIMESTAMP}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Documento encontrado en MongoDB'
    assert 'element' in json_data

def test_btcars_GET_BTCars_not_found(app, client):
    response = client.get('/btcars/1234567890')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['message'] == 'Documento no encontrado en MongoDB'
    assert json_data['element'] == {}

def test_btcars_GET_BTCars_invalid_timestamp(app, client):
    response = client.get('/btcars/invalid')
    assert response.status_code == 404

#
# Pruebas unitarias para el cálculo de promedio
#

def test_btcars_promedio_success(app, client):
    response = client.get(f'/btcars/promedio?init={TEST_INIT_VALUE}&end={TEST_END_VALUE}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Promedio obtenido exitosamente.'
    assert 'prom' in json_data

def test_btcars_promedio_no_docs(app, client):
    response = client.get('/btcars/promedio?init=1416519438&end=1316522306')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['message'] == 'No existen documentos para el rango solicitado.'
    assert json_data['prom'] is None

def test_btcars_promedio_invalid_range(app, client):
    response = client.get(f'/btcars/promedio?init={TEST_END_VALUE}&end={TEST_INIT_VALUE}')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['message'] == 'Búsqueda mal formada. end debe ser mayor que init.'
    assert json_data['prom'] is None

def test_btcars_promedio_missing_params(app, client):
    response = client.get('/btcars/promedio')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['message'] == 'Consulta mal formada. Se requieren parametros init Y end'
    assert json_data['prom'] is None

#
# Pruebas unitarias para función de paginación
#

def test_btcars_pagination_with_timestamps_success(app, client):
    response = client.get(f'/btcars?page={TEST_PAGE_VALUE}&init={TEST_INIT_VALUE}&end={TEST_END_VALUE}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Documentos obtenidos con filtro de timestamp.'
    assert 'elements' in json_data

def test_btcars_pagination_without_timestamps_success(app, client):
    response = client.get(f'/btcars?page={TEST_PAGE_VALUE}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Documentos obtenidos sin filtro de timestamp.'
    assert 'elements' in json_data

def test_btcars_pagination_invalid_page(app, client):
    response = client.get('/btcars?page=-1&init=1716519438&end=1716522306')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['message'] == 'La página no puede ser menor que 1'
    assert json_data['elements'] is None

def test_btcars_pagination_missing_page(app, client):
    response = client.get('/btcars?init=1716519438&end=1716522306')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['message'] == 'Se necesita parámetro page para paginación'
    assert json_data['elements'] is None