from fastapi import status

def test_correct_logout(client, mocked_user2_logged_in):
    response = client.post("/user_logout", data={'id': 2})
    assert response.json() == {'detail': "Usuario deslogeado correctamente"}
    assert response.status_code == status.HTTP_200_OK

def test_user_not_logged_in(client, mocked_user1):
    response = client.post("/user_logout", data={'id': 1})
    assert response.json() == {'detail': "Usuario no está actualmente logeado"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_user_doesnt_exist(client):
    response = client.post("/user_logout", data={'id': 1})
    assert response.json() == {'detail': "Usuario no existe"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST