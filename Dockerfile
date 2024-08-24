# Usa una imagen base de FastAPI con Python 3.11
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todo el contenido del proyecto en el contenedor
COPY . /app

# Instala las dependencias si tienes un archivo requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto para iniciar Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
