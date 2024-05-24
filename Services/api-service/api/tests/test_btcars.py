
def test_btcars_GET_BTCars(app,client):
    response = client.get('/btcars/1716517049')
    assert response.status_code == 200