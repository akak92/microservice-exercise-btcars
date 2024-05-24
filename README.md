# microservice-exercise-btcars
Microservicio que permite obtener el precio actual de bitcoin cada N segundos. Permitiendo realizar búsquedas mediante la consulta a una API REST.

Las consultas requieren de la utilización de un timestamp para filtrado. El formato esperado del timestamp es el `Formato de fecha: Tiempo Unix`. Para saber más visite [este enlace](https://es.wikipedia.org/wiki/Tiempo_Unix).

#### Herramientas / Frameworks

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
ren .env.example .env
```
#### En Linux:
```
mv .env.example .env
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

#Parámetros para pruebas unitarias
TEST_INIT_VALUE=
TEST_END_VALUE=
TEST_TIMESTAMP=
TEST_PAGE_VALUE=

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

El microservicio es subdividido en 3 diferentes services (contenedores).

* `Servicio request:` Posee un script `main.py` que se ejecuta cada N segundos. Realiza la consulta a URL que nos provee de los precios de bitcoin. Establece conexión a base local MongoDB y almacena los valores del elemento "btcars". Se añade campo "timestamp" al documento "btcars" con el timestamp correspondiente a la realización de la consulta `(formato Unix [integer], horario local).`

* `Servicio mongo:` Base de datos no relacional que posee una colección llamada `btcars`. Allí almacenamos elementos obtenidos por el servicio request. Es utilizada por el servicio api para consultar la información.

* `Servicio api:` API REST escrita en Flask para la realización de diversas consultas. Utiliza el servicio mongo como fuente de información.

Los servicios `api` y `request` dependen de `mongo`. Se utiliza la cláusula `depends_on` dentro de docker-compose para garantizar que el servicio mongo inicie primero.

Esta división en diferentes servicios mejora el mantenimiento y ciclo de vida general de la aplicación.

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

Las pruebas unitarias se han definido para el `servicio api` dentro de la carpeta `tests` utilizando la librería `pytest`.

Dentro del archivo `.env` se encuentran variables que deben ser completadas previas a la ejecución de las pruebas.

```
[...]
#Parámetros para pruebas unitarias
TEST_INIT_VALUE=
TEST_END_VALUE=
TEST_TIMESTAMP=
TEST_PAGE_VALUE=
```
Una vez cargadas estas variables, volver a encender el contenedor.

Para ejecutar las pruebas, abrir una shell y ejecutar el comando:
```
docker exec -it microservice-exercise-btcars-api-1 pytest /app/api/tests/test_btcars.py
```

Puede que el nombre del contenedor cambie (en algunos sistemas el nombre utiliza `_` en vez de `-`). Consulte el nombre del contenedor del servicio api utilizando el comando `docker ps`

#### Aclaración sobre pruebas unitarias

Observarán que se producen múltiples advertencias (warnings). Esto se debe a conflictos entre las versiones recientes de flask `[Flask>=3.0]` y la versión de flask-mongoengine instalada en mi PC local `[flask-mongoengine==1.0.0]`.

Por cuestiones de tiempo y al tener un plazo de 3 días, decidí utilizar `Flask==2.2.2` para evitar problemas de compatibilidad (problemas con `JSONEncoder` al parecer).




