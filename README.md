Optidata
========

**Optidata** est un projet universitaire conçu pour répondre aux besoins réels des petites et moyennes entreprises (PME).  
L'objectif est de fournir une solution intégrée basée sur **Docker**, embarquant des services tels que **NiFi**, **MySQL**, et une interface web.

---

**Description du Projet**
-------------------------

Ce projet vise à intégrer les données d'une entreprise afin de les gérer via un workflow NiFi.  
Le workflow permet de traiter les données, puis de les enregistrer dans une base de données MySQL dédiée.

Les données brutes ne sont pas stockées directement dans le dépôt GitHub en raison de leur taille.  
Un Google Drive est utilisé pour stocker et partager ces fichiers :  
`Lien vers le Google Drive <https://drive.google.com/drive/folders/1f5ePEdOSBNZsO4NQhb4iMCa4DmaReMID?dmr=1&ec=wgc-drive-globalnav-goto>`_

---

**Fonctionnalités principales**
-------------------------------

- Conteneurisation des services avec Docker.
- Gestion et transformation des données avec NiFi.
- Stockage structuré des données dans une base MySQL.
- Possibilité d'ajouter une interface web pour la visualisation et l'interaction.

---

**Prérequis**
-------------

- **Docker** installé sur votre machine.
- Une connexion à Google Drive pour récupérer les fichiers d'exemple.
- Accès à l'image NiFi et MySQL via Docker Hub.

---

**Étapes pour Utiliser le Projet**
----------------------------------

1. **Cloner le dépôt GitHub**  
   Clonez le projet sur votre machine locale :  
   ``git clone https://github.com/SteveHoareau18/optidata.git``

2. **Récupérer les fichiers sur Google Drive**  
   <https://drive.google.com/drive/folders/1f5ePEdOSBNZsO4NQhb4iMCa4DmaReMID?dmr=1&ec=wgc-drive-globalnav-goto>

3. **Placer les fichiers au bon endroit**   
   Placez-les dans les répertoires désignés :
   Le fichier Excel --> ``optidata/nifi/fichier_excel``
   Télécharger l'image NIFI dans l'environnement en éxécutant la commande suivante --> ``docker load chemin/vers/nifi_optidata.tar nifi_optidata:latest``

5. **Lancer les services**  
   Exécutez la commande suivante pour démarrer les conteneurs Docker :  
   ``docker-compose --env-file .env-prod up -d``

6. **Configurer NiFi**  
   Accédez à l'interface de NiFi via ``http://localhost:8443`` et configurez les workflows en important le fichier json présent sur le drive ( NIFI_OPTIDATA.json par exemple ) 

7. **Importer les données dans MySQL**  
   - Vérifiez que votre base de données est prête à recevoir les données en observant le service associé. Ce dernier doit être au staut "enabled".
   - Configurez une table dédiée en fonction des besoins du workflow si elle n'existe pas encore.

8. **Visualiser et analyser les données**  
   Une fois les données intégrées, vous pouvez les analyser directement dans MySQL ou via l'interface web si configurée.

---

**Notes Importantes**
---------------------

- Les workflows NiFi peuvent être exportés et importés au format XML/JSON pour partage et réutilisation.

---

**Contact**
-----------

Pour toute question ou contribution, contactez-nous via notre dépôt GitHub ou l'adresse e-mail associée au projet.






### récupérer l'image pour pouvoir lancer le docker docker-compose --env-file .env-prod up
docker load nifi_optidata.tar nifi_optidata:latest
