#
#   Pedro Díaz | 23-05-2023
#   Test unitarios para funcion promedio  
#   

def test_btcars_promedio_success(app, client):
    response = client.get('/btcars/promedio?init=1716519438&end=1716522306')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Promedio obtenido exitosamente.'
    assert 'prom' in json_data

def test_btcars_promedio_no_docs(app, client):
    response = client.get('/btcars/promedio?init=1716519438&end=1716522306')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['message'] == 'No existen documentos para el rango solicitado.'
    assert json_data['prom'] is None

def test_btcars_promedio_invalid_range(app, client):
    response = client.get('/btcars/promedio?init=1716522306&end=1716519438')  # init > end
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