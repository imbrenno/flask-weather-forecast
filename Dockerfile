# Usar uma imagem base do Python
FROM python:3.11.7

ENV PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .env

ENV FLASK_APP=run.py

EXPOSE 5000

CMD ["python", "run.py"]
