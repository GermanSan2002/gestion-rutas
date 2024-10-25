# Microservicio de Gestión de Rutas

Este proyecto implementa un microservicio para la gestión de rutas en una aplicación minera, utilizando **Python** y **FastAPI**. El microservicio se encarga de proporcionar rutas óptimas, seguimiento vehicular en tiempo real, y visualización de puntos de interés (POI) en el mapa.

## Estructura de Archivos del Proyecto

```
project-root/
├── app/
│   ├── __init__.py                 # Permite que "app" se trate como un paquete.
│   ├── main.py                      # Punto de entrada de la aplicación FastAPI.
│   ├── config.py                    # Configuración de variables de entorno y API keys.
│   ├── routers/                     # Contiene los archivos de enrutamiento (endpoints).
│   │   └── routes.py                # Endpoints para obtener rutas, seguimiento en tiempo real y POIs.
│   ├── services/                    # Lógica de negocio, integraciones con APIs externas.
│   │   ├── maps_service.py          # Lógica de integración con Google Maps o Mapbox.
│   │   ├── weather_service.py       # Lógica para obtener datos de clima en tiempo real.
│   │   └── tracking_service.py      # Lógica para seguimiento vehicular en tiempo real.
│   ├── models/                      # Modelos de datos (schemas, DTOs, entidades).
│   │   ├── route_model.py           # Definición de datos para las rutas.
│   │   ├── poi_model.py             # Definición de datos para los puntos de interés.
│   │   └── tracking_model.py        # Definición de datos para el seguimiento de vehículos.
│   ├── utils/                       # Funciones utilitarias para manejo de errores y autenticación.
│   │   └── error_handler.py         # Gestión de errores y excepciones.
│   ├── db/                          # Configuración de la base de datos.
│   │   ├── connection.py            # Conexión y configuración de la base de datos.
│   │   └── models.py                # Definición de modelos de base de datos (ORM).
├── tests/                           # Pruebas unitarias y de integración.
│   ├── test_routes.py               # Pruebas para los endpoints de rutas.
│   ├── test_tracking.py             # Pruebas para el seguimiento en tiempo real.
│   └── test_poi.py                  # Pruebas para la gestión de puntos de interés.
├── .env                             # Variables de entorno (API keys, configuración de DB).
├── Dockerfile                       # Configuración para despliegue en contenedor.
├── docker-compose.yml               # Configuración para orquestar servicios (Redis, DB).
└── requirements.txt                 # Lista de dependencias y paquetes.
```

### Función de Cada Archivo

#### Directorio `app/`
- **`__init__.py`**: Marca `app` como un paquete, permitiendo la importación de módulos y archivos de forma jerárquica.
- **`main.py`**: Punto de entrada de la aplicación FastAPI. Aquí se inicializa la aplicación, se configuran las rutas, y se habilitan la documentación Swagger y el manejo global de errores.
- **`config.py`**: Carga de variables de entorno, como la API key de Google Maps, configuración de base de datos y cualquier clave de acceso a otros servicios. Facilita la seguridad y modularidad del código.

#### Subdirectorio `routers/`
- **`routes.py`**: Define los endpoints principales del microservicio, como la obtención de rutas, el seguimiento de vehículos en tiempo real, y la visualización de puntos de interés. Usa las funciones de los servicios para responder a las solicitudes HTTP.

#### Subdirectorio `services/`
- **`maps_service.py`**: Implementa la lógica para obtener rutas utilizando Google Maps, Mapbox, u otro proveedor. Esta clase interactúa con la API de mapas para recuperar direcciones, calcular distancias, tiempos de viaje y puntos de ruta.
- **`weather_service.py`**: Lógica para obtener y procesar datos climáticos, integrándose con una API meteorológica para obtener el clima actual y pronósticos relevantes.
- **`tracking_service.py`**: Gestiona el seguimiento en tiempo real de vehículos o activos, registrando posiciones actuales y rutas recorridas para proporcionar visibilidad de localización en el frontend.

#### Subdirectorio `models/`
- **`route_model.py`**: Define el esquema y modelo de datos de las rutas, incluyendo campos como origen, destino, puntos de paso y tiempo estimado de llegada.
- **`poi_model.py`**: Define el esquema para los puntos de interés (POIs), con datos como nombre, ubicación, y tipo (centro de salud, taller mecánico, etc.).
- **`tracking_model.py`**: Modelo para representar datos de seguimiento en tiempo real, como ubicación actual, estado del vehículo y tiempos de parada.

#### Subdirectorio `utils/`
- **`error_handler.py`**: Contiene manejadores de errores personalizados y excepciones para respuestas HTTP coherentes, mejora la experiencia del usuario y ayuda en la depuración.

#### Subdirectorio `db/`
- **`connection.py`**: Configura y establece la conexión a la base de datos, manejando la creación de conexiones y su reaprovechamiento.
- **`models.py`**: Define los modelos de base de datos necesarios para el microservicio, permitiendo guardar, consultar y actualizar datos como el historial de rutas y ubicaciones de vehículos.

#### Directorio `tests/`
- **`test_routes.py`**: Contiene pruebas unitarias y de integración para los endpoints de rutas, validando la obtención de rutas desde diferentes orígenes y destinos.
- **`test_tracking.py`**: Pruebas para el seguimiento en tiempo real, evaluando la precisión y disponibilidad de datos de ubicación y tiempos de parada.
- **`test_poi.py`**: Verifica la funcionalidad de puntos de interés, comprobando que los POIs pueden ser agregados y visualizados correctamente.

#### Archivos en el nivel raíz
- **`.env`**: Almacena variables sensibles como claves API y credenciales de base de datos, permitiendo mantener la seguridad y modularidad del código.
- **`Dockerfile`**: Define la configuración para crear la imagen Docker del microservicio, incluyendo instalación de dependencias y configuración del servidor.
- **`docker-compose.yml`**: Orquesta servicios como Redis (para caché de rutas frecuentes) o la base de datos, facilitando el despliegue y administración de recursos en contenedores.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el microservicio, como FastAPI, googlemaps, SQLAlchemy, entre otras.