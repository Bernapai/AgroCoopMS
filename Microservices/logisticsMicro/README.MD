# Servicio de Logística (Logistics) 🚚

Microservicio encargado de la gestión de envíos y transporte de productos.

## Funcionalidades
- Gestión de envíos de productos.
- Registro de entregas completadas.

## Endpoints
- `GET /logistics`: Lista todos los envíos.
- `GET /logistics/{id}`: Lista un envío.
- `POST /logistics`: Crea un nuevo envío.
- `PUT /logistics/{id}`: Actualiza el estado de un envío.
- `DEL /productos/{id}`: Elimina un envio.

## Tecnologías Utilizadas
- **FastAPI**
- **MongoDB**
- **Docker**