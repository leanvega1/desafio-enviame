## Ejercicio 1:

## Stack utilizado: Python, Django, Postgres, Nginx
## para levantar el proyecto se deben correr los siguentes comandos en el orden colocado

## crear entorno
python3 -m venv myvenv

## ingresar al entorno
source myvenv/bin/activate

## instalar docker https://docs.docker.com/engine/install/ubuntu/

## instalar docker compose https://docs.docker.com/compose/install/

## correr migraciones
docker-compose run django_app python mysite/manage.py migrate

## archivos estáticos
docker-compose run django_app python mysite/manage.py collectstatic

## levantar el proyecto
docker-compose up --build

## url: http://0.0.0.0:8000/admin/

# --------------------------------------------------------------------------------------------- #

## Ejercicio 2:

## levantar el proyecto
docker-compose up --build

## en otra shell, para correr el script que genera 20 instancias fake de Empresa
docker exec -it app-django_django_app_1 bash
cd mysite
python3 manage.py shell
exec(open('generate_faker.py').read())
exit()
exit

## url api de las empresas: http://0.0.0.0:8000/api_rest/company/
## url para ver una empresa en particular: http://0.0.0.0:8000/api_rest/company/id/ - ej: http://0.0.0.0:8000/api_rest/company/3/ 



