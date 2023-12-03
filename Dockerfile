FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copier le dossier 'templates'
COPY templates ./templates

# Exposer le port 5000
EXPOSE 5000

CMD ["python", "./app.py"]
