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
## Descripción

El microservicio es subdividido en 3 diferentes servicios (contenedores) que, operando de forma conjunta, ofrecen una solución modular para facilitar su modificación y/o mantenimiento.

* `Servicio request:` Posee un script `main.py` que se ejecuta cada N segundos. Realiza consulta a endpoint de API provista sobre los precios de bitcoin. Establece conexión a base local MongoDB y almacena los valores del elemento "btcars". Se añade campo "timestamp" al documento "btcars" con el timestamp correspondiente a la realización de la consulta `(formato Epoch: número entero, horario local).`

* `Servicio mongo:` Base de datos no relacional que posee una colección llamada `btcars`. Allí almacenamos elementos obtenidos por el servicio request. Es utilizada por el servicio api para consultar la información.

* `Servicio api:` API REST escrita en Flask para la realización de diversas consultas. Utiliza el servicio mongo como fuente de información.

Los servicios `api` y `request` dependen de `mongo`. Se utiliza la cláusula `depends_on` dentro de docker-compose para garantizar que el servicio mongo inicie primero.

A continuación se adjunta un diagrama que acompaña lo descrito previamente:
![Diagrama de solución](docs/diagrama.png)

## Utilización con POSTman

En el repositorio, existe una colección almacenada llamada `BTCars - Microservicio.postman_collection.json` en la que se encuentran definidos los endpoints para realizar pruebas.

Ingrese a POSTMan e importe la colección. Deberá cambiar el valor de una serie de variables definidas para la colección:

```
    LOCAL_IP : Su dirección ip local
    timestamp : timestamp que utilizará en el / los endpoints
    init : timestamp de inicio de rango de búsqueda
    end : timestamp de finalización de rango de búsqueda
    page : página a la cual desea acceder en endpoint de paginación
```

#### Obtener Dirección IP local

#### Windows

Abra PowerShell, ejecute el siguiente comando:
```
Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias "Wi-Fi" | Select-Object -ExpandProperty IPAddress
```
En caso de estar conectado por cable (Ethernet), reemplace `"Wi-Fi"` por `"Ethernet"`.

#### Linux

Abra una shell, ejecute el siguiente comando:
```
ip addr show wlan0 | grep inet
```
En caso de estar conectado por cable (Ethernet), reemplace `wlan0` por `eth0`.

## Pruebas Unitarias

Las pruebas unitarias se han definido para el `servicio api` dentro de la carpeta `tests` utilizando la librería `pytest`

Para ejecutar las pruebas, abrir una shell y ejecutar el comando:
```
docker exec -it microservice-exercise-btcars-api-1 pytest /app/api/tests/test_btcars.py
```

Puede que el nombre del contenedor cambie. En cualquier caso, consulte el nombre del contenedor del servicio api utilizando el comando `docker ps`

#### Aclaración sobre pruebas unitarias

Observarán que se producen múltiples advertencias (warnings).
Esto se debe a la versión de Flask utilizada. `Flask==2.2.2`




