from main import app
from fastapi.testclient import TestClient
from src.db import db_test, reset_db_test

client = TestClient(app)

def test_your_endpoint():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_register_user():
    db_test.connect()
    response = client.post('/register_user', data={"name":"GoodName", "lastname":"GoodLastname","email":"goodemail@mail.com","password":"GooDpaSsword1"})
    assert response.json() == {"detail":"User Created"}
    assert response.status_code == 201
    reset_db_test()

def test_mynumber():
    response = client.post('/mytest/', data={'numero': "aaa"})
    assert response.json() == {"detail": "aaa"}
    assert response.status_code == 201

db_test.close()