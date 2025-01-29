# Usar una imagen base de Python (puedes elegir otra versión si es necesario)
FROM python:3.10-slim


# Define el directorio de trabajo en el contenedor
WORKDIR /main

# Copia los archivos del proyecto al directorio de trabajo
COPY . /main

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto donde correrá FastAPI
EXPOSE 8002

# Comando para iniciar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
