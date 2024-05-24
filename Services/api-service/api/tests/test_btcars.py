#
#   Pedro Díaz | 23-05-2023
#   Test unitarios para controlador BTCars definido en controllers   
#   

def test_btcars_GET_BTCars(app,client):
    response = client.get('/btcars/1716517049')
    assert response.status_code == 200

def test_btcars_promedio(app,client):
    response = client.get('/btcars/promedio?init=1716519438&end=1716522306')
    assert response.status_code == 200

def test_btcars_pagination_with_timestamps(app,client):
    response = client.get('/btcars?page=1&init=1716519438&end=1716522306')
    assert response.status_code == 200

