#!/bin/bash
# Démarrer NiFi
/opt/nifi/bin/nifi.sh start

# Attendre quelques secondes pour s'assurer que NiFi a démarré
sleep 10

# Définir l'utilisateur et le mot de passe
/opt/nifi/bin/nifi.sh set-single-user-credentials optidata 5f4oZ682Jh09k5w
