import pytest
from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from main import app
# from models import Post,User 

@pytest.fixture(scope="function")
def client() -> TestClient:
    "start the client"
    return TestClient(app)

# @pytest.fixture()
# def setUp(client:TestClient):

#     response_user = client.post('/jsonPlaceHolder/crea_users')
#     print(response_user)
def test_user(client:TestClient):
    response_user = client.post('/jsonPlaceHolder/crea_users')
    assert response_user.json()["respuesta"]=='Usuarios creados satisfactoriamente!'

def test_todos(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_todos')
    assert response.json()["respuesta"]=='Todos creados satisfactoriamente!'

def test_album(client:TestClient):
    response =  client.post('/jsonPlaceHolder/crea_albums')
    assert response.json()["respuesta"]=='Albumns creados satisfactoriamente!'

def test_fotos(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_fotos')
    assert response.json()["respuesta"]=='Photos creados satisfactoriamente!'

def test_post(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_post')
    assert response.json()["respuesta"]=='Post creados satisfactoriamente!'

def test_comentarios(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_comentarios')
    assert response.json()["respuesta"]=='Comments creados satisfactoriamente!'

# def test_elimina_todo(client:TestClient):
#     response =  client.delete('/jsonPlaceHolder/elimina_todo')
#     assert response.json()["respuesta"] == 'Todo eliminado con exito!'

# def test_crea_todo(client:TestClient):
#     response =  client.post('/jsonPlaceHolder/crear_todo')
#     assert response.json()["respuesta"] =='Todo creado con exito!'

def test_user_id(client:TestClient):
    response = client.get('/user/1')
    assert "name" in response.json()
    assert response.json()["email"] == 'Sincere@april.biz'

def test_album_id(client:TestClient):
    response = client.get('/album/1')
    assert "title" in response.json()
    assert response.json()["title"] == 'quidem molestiae enim'
    assert response.json()["userId"] == 1

def test_post_id(client:TestClient):
    response = client.get('/posts/1')
    assert "title" in response.json()
    assert response.json()["id"] == 1
