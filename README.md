# Sistema de Gestión para Cooperativas Agrícolas 🌾🚜

Este proyecto es una solución backend basada en microservicios para la gestión de cooperativas agrícolas. Utiliza **FastAPI** para los microservicios, **MongoDB** como base de datos , **RabbitMQ** para la comunicacion entre los microservicios y **Docker** para contenerizar cada componente del sistema. Además, se ha implementado una **API Gateway** para manejar la autenticación, autorización y redirección de los servicios.

## Arquitectura 🏗️

El sistema se divide en varios microservicios, cada uno encargado de diferentes aspectos de la cooperativa agrícola:

1. **API Gateway(Kong)** 🌐  
   - Redirige las solicitudes a los microservicios correspondientes.(Kong)
   - Maneja la autenticación y autorización mediante tokens JWT. (Kong)

2. **Microservicios** 🖥️:
   - **Servicio de Gestión de Socios (Farmers)** 🚶‍♂️🚶‍♀️  
     Endpoints: `/farmers`  
     Funcionalidad: Gestión de usuarios y socios de la cooperativa.
     
   - **Servicio de Cultivos (Crops)** 🌱  
     Endpoints: `/crops`  
     Funcionalidad: Información y seguimiento de cultivos agrícolas.
     
   - **Servicio de Logística (Logistics)** 🚚  
     Endpoints: `/logistics`  
     Funcionalidad: Gestión de envíos y transporte de productos.

   - **Servicio de Ventas y Reportes Financieros (Sales)** 💰📊  
     Endpoints: `/sales`  
     Funcionalidad: Control de ventas y generación de reportes financieros.

   - **Servicio de Productos (Products)** 🛒🌾  
     Endpoints:** `/productos`  
     Funcionalidad:** Gestión de inventario, registro de productos, consulta, actualización de stock y eliminación de productos.  

  



## Tecnologías Utilizadas 🔧

- **FastAPI**: Framework para construir APIs rápidas y eficientes.
- **MongoDB**: Base de datos NoSQL utilizada en cada microservicio.
- **Docker**: Contenerización de cada microservicio y su base de datos.
- **JWT (JSON Web Tokens)**: Autenticación y autorización de usuarios.
- **API Gateway**: Manejo centralizado de solicitudes y redirección de microservicios.
- **RabbitMQ**: Comunicacion entre microservicios.
- **Kong**: Desplega la API Gateway

