#
#   Pedro Díaz | 23-05-2023
#   Test unitarios para funcion GET_BTCars  
#   

def test_btcars_GET_BTCars_success(app, client):
    response = client.get('/btcars/1716517049')
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
    assert response.status_code == 400

