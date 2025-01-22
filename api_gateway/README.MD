# API Gateway 🌐

Este componente actúa como punto de entrada principal para el sistema de gestión de cooperativas agrícolas. Redirige solicitudes a los microservicios correspondientes y maneja la autenticación y autorización mediante tokens JWT.

## Funcionalidades
- Redirección de solicitudes a microservicios (`farmers`, `inventory`, `logistics`, `ventas`).
- Manejo de autenticación y autorización con JWT.
- Protección de rutas según los permisos de usuario.

## Endpoints Principales
- `/auth/login`: Autenticación de usuario.
- `/auth/register`: Registro de nuevos usuarios.
- `/auth/refresh`: Renovación de tokens JWT.

## Tecnologías Utilizadas
- **FastAPI**
- **JWT (JSON Web Tokens)**
- **Docker**
