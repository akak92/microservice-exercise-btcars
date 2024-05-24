#
#   Pedro Díaz | 23-05-2023
#   Test unitarios para funcion de paginación  
#   


def test_btcars_pagination_with_timestamps_success(app, client):
    response = client.get('/btcars?page=1&init=1716519438&end=1716522306')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Documentos obtenidos con filtro de timestamp.'
    assert 'elements' in json_data

def test_btcars_pagination_without_timestamps_success(app, client):
    response = client.get('/btcars?page=1')
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