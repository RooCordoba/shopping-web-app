from fastapi import status

def test_email_doesnt_exist(client):
    response = client.post('/user_login', data={'email':"emailDoes@notexist", 'password':"aPassworD123"})
    assert response.json() == {'detail':'Email no registrado'}
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_password_doesnt_match(client,mocked_user1):
    response = client.post('/user_login', data={'email':"mocked@email", 'password':"notThePassword123"})
    assert response.json() == {'detail':'La contraseña no coincide con el email ingresado'}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_correct_login(client,mocked_user1):
    response = client.post('/user_login', data={'email':"mocked@email", 'password':"asdASD123"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'detail':'Usuario logeado correctamente'}