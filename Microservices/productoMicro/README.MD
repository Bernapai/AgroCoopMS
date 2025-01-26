
# Servicio de Gestión de Productos (Products) 🛒🌾

Microservicio encargado de la gestión del inventario de productos de la cooperativa.

## Funcionalidades
- Registro de productos.
- Consulta de productos y stock.
- Actualización de información y stock.
- Eliminación de productos.

## Endpoints
- `GET /productos`: Lista todos los productos.
- `POST /productos`: Registra un nuevo producto.
- `PUT /productos/{producto_id}`: Actualiza la información de un producto.
- `DELETE /productos/{producto_id}`: Elimina un producto del inventario.

## Tecnologías Utilizadas
- **FastAPI**
- **MongoDB**
- **Docker**
