1. Solicitar datos a la api y guardar la informacion en la bd
2. Creacion de apis


- Iniciar con alembic 
    alembic init alembic
    modificiar el alembic.ini
    alembic revision --autogenerate -m 'crear modelos'
    alembic upgrade heads

La carpeta repository se encarga de las consultas
la carpeta routers se encarga de las rutas de la api
- Instalar dependencias
    pip install -r requirments.txt
Ejecutar app (entrar a la carpeta app ):
    uvicorn main:app --reload

Tener en cuenta que si se ejecuta cualquiera api de PlaceHolder Api esta eliminara todos los registros de la tabla para volverlos a cargar
y a su vez si tienen referencia en otras tabla ese id , se eliminara ya que esta en cascade.

Funcion create_todo 
    se penso consumir la api pero ese proceso tardaba mucho por eso se llamo a la funcion y el tiempo disminuia


graphql
    http://localhost:8000/graphql
    
    mutacion crear post ejemplo :
        mutation CreateNewPost{
            createNewPost(title:"Este es un nuevo post", body:"nuevo post",userId:1) {
                ok
            }
        }
    
    Mutacion crear album:
        mutation {
            createNewAlbum(title:"Este es un nuevo post",userId:1) {
                ok
            }
        }
    query todos los post ejemplo:
        query{
            allPosts{
                title
            }
        }
    query trae todos los albums:           
        query{
            allAlbums{
                title
                id
            }
        }

resolve_ -> al inicio de una query es importante porque es lo que va a devolver

## Ejecutar test 
    estar en la carpeta app y ejecutar
    - pytest test_api.py
    - pytest test_graphql.py
    o
    pytest
    Tener en cuenta que cuando se ejecuta el test test_graphql.py al menos las tablas de las base de datos deben de estar llenas

## Eliminar todas las imágenes de docker
    docker rmi $(docker images -q)

## Eliminar todos los contenedores de docker
    docker rm $(docker ps -a -q)

## Correr docker-compose

    docker-compose up --build

    Cuando ya todo este corriendo entrar al contendor que corre la aplicacion de fastapi con el siguiente comando
        docker exec -it --user root d6fd6c557b52 /bin/bash

    y luego ejecutar

    alembic revision --autogenerate -m 'crear modelos'
    alembic upgrade heads

    por ultimo salir del contenedor

    exit
    
    Importante:
        Si desea hacer cambios en los modelos antes de volver a realizar las migraciones debe de eliminar la tabla alembic de la base de datos y luego si realizar la migracion correspondiente.
        


