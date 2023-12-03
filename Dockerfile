FROM python:3.8

# Créer un utilisateur non privilégié
RUN useradd -m myuser
USER myuser

WORKDIR /home/myuser/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Créez un répertoire 'output' avec des autorisations suffisantes
RUN mkdir /home/myuser/app/output && chmod 777 /home/myuser/app/output

CMD ["python", "./app.py"]
