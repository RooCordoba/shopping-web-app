from fastapi import status

def test_register_user(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {"detail":"User Created"}
    assert response.status_code == status.HTTP_201_CREATED

def test_user_exists(client, mocked_user1):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"mocked@email","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "User already exist"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_short_name(client):
    response = client.post('/register_user', data={"name":"no", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "Nombre debe contener entre 3 y 15 caracteres"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_long_name(client):
    response = client.post('/register_user', data={"name":"aVeryveryveryveryveryveryverylongname", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "Nombre debe contener entre 3 y 15 caracteres"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_short_last_name(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"a","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "Apellido debe contener entre 3 y 20 caracteres"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_long_last_name(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"aVeryveryveryveryveryveryverylonglastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {'detail': "Apellido debe contener entre 3 y 20 caracteres"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_short_password(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"short"})
    assert response.json() == {'detail': "El password debe de contener minimo 6 caracteres"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_invalid_password_Upper(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"invalidpassword"})
    assert response.json() == {'detail': "La contraseña debe tener minimo una mayuscula, una minuscula y un numero" }
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_invalid_password_lower(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"INVALIDPASSWORD"})
    assert response.json() == {'detail': "La contraseña debe tener minimo una mayuscula, una minuscula y un numero" }
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_invalid_password_number(client):
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"inValidPassWord"})
    assert response.json() == {'detail': "La contraseña debe tener minimo una mayuscula, una minuscula y un numero" }
    assert response.status_code == status.HTTP_400_BAD_REQUEST