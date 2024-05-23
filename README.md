# microservice-exercise-btcars
Creación de microservicio, obteniendo información de API sobre precios de Bitcoin

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Pre - requisitos

Tener instalados Docker & docker-compose. Para mayor información, visite [este enlace](https://docs.docker.com/manuals/).

Tener instalado Git. Puede descargarlo [aquí](https://git-scm.com/downloads)

## Instalación

Descargue el repositorio utilizando el siguiente comando:
```
git clone https://github.com/akak92/microservice-exercise-btcars.git
```

Diríjase al directorio del repositorio utilizando el comando `cd` y cambie el nombre del archivo `.env.example` a `.env`

#### En Windows:
```
mv .env.example .env
```
#### En Linux:
```
ren .env.example .env
```

#### Archivo .env

Aquí se encuentran alojadas las variables de entorno que luego son utilizadas por los distintos servicios.
```
DB_USER=your_db_user
DB_PASSWD=your_db_password
DB_COLLECTION=your_db_collection
URL=https://be.buenbit.com/api/market/tickers/

DEFAULT_PAGE_SIZE=10 # Tamaño utilizado para paginación

SLEEP_TIME_IN_SECONDS=10 #cantidad de segundos para solicitud request.
```
Por defecto, ya existen valores cargados para un correcto funcionamiento del aplicativo.

#### Inicializar los servicios

Ejecute el siguiente comando para inicializar los contenedores:
```
docker-compose up --build --remove-orphans -d
```
El contenedor se inicializará en segundo plano, gracias al argumento `-d`. Recuerde que para ver los logs de los servicios puede utilizar el comando:
```
docker logs <NOMBRE_DEL_CONTENEDOR>
```

