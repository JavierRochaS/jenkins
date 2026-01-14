FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY main.py .
CMD ["python", "-u", "main.py"]
