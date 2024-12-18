#!/bin/bash

# Variables
NIFI_HOME="/home/optidata/nifi"
NIFI_BIN="$NIFI_HOME/bin/nifi.sh"

# Vérifier si le fichier exécutable existe
if [[ ! -f "$NIFI_BIN" ]]; then
  echo "Erreur : Le script nifi.sh n'a pas été trouvé dans $NIFI_BIN."
  exit 1
fi

# Actions possibles
case "$1" in
  start)
    echo "Démarrage d'Apache NiFi..."
    $NIFI_BIN start
    ;;
  stop)
    echo "Arrêt d'Apache NiFi..."
    $NIFI_BIN stop
    ;;
  status)
    echo "Vérification du statut d'Apache NiFi..."
    $NIFI_BIN status
    ;;
  restart)
    echo "Redémarrage d'Apache NiFi..."
    $NIFI_BIN stop
    sleep 2
    $NIFI_BIN start
    ;;
  help|*)
    echo "Utilisation : $0 {start|stop|status|restart|help}"
    exit 1
    ;;
esac

exit 0
