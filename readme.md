1. Solicitar datos a la api y guardar la informacion en la bd
2. Creacion de apis


- Iniciar con alembic 
    alembic init migrations
    modificiar el alembic.ini
    alembic revision --autogenerate -m 'create user model2'
    alembic upgrade heads

La carpeta repository se encarga de las consultas
la carpeta routers se encarga de las rutas de la api
- Instalar dependencias
    pip install -r requirments.txt
Ejecutar app (entrar a la carpeta app ):
    uvicorn main:app --reload

Tener en cuenta que si se ejecuta cualquiera api de PlaceHolder Api esta eliminara todos los registros de la tabla para volverlos a cargar
y a su vez si tienen referencia en otras tabla ese id , se eliminara ya que esta en cascade.

