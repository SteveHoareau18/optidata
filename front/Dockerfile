<<<<<<< HEAD
=======
# Utiliser une image Python 3.10 slim
FROM python:3.10-slim

# Installer Git (et autres dépendances système si besoin)
RUN apt-get update && apt-get install -y git && apt-get clean

# Créer un environnement virtuel dans /opt/venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Définir le répertoire de travail dans l'image
WORKDIR /opt/app

# Copier les fichiers du contexte de build dans l'image
COPY requirements.txt /opt/app/
COPY optidata_project/ /opt/app/optidata_project/

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Se placer dans le répertoire du projet Django
WORKDIR /opt/app/optidata_project/

# Exécuter les migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Exposer le port utilisé par Django
EXPOSE 8000

# Lancer le serveur de développement Django
CMD ["python", "manage.py", "runserver","localhost:8000"]
>>>>>>> 0e2fcc9 (fix token in project)
