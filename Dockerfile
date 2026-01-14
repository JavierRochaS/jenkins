# Usar imagen ligera de Python
FROM python:3.11-slim

# Configurar variables de entorno para ver logs en Jenkins
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Copiar el script al contenedor
COPY main.py .

# Comando de ejecución
CMD ["python", "-u", "main.py"]
