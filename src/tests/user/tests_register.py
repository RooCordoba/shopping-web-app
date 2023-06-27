

def test_register_user(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {"detail":"User Created"}
    assert response.status_code == 201

def test_short_name(client):
    response = client.post('/register_user', data={"name":"no", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "Nombre debe contener entre 3 y 15 caracteres"}
    assert response.status_code == 400

def test_long_name(client):
    response = client.post('/register_user', data={"name":"Averyveryveryveryveryveryverylongname", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "Nombre debe contener entre 3 y 15 caracteres"}
    assert response.status_code == 400
