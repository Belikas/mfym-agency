#!/bin/sh
# Exécute workflow.json avec la vraie CLI n8n (version épinglée), sans compte ni serveur. Sortie complète dans out/n8n-execution.log
cd "$(dirname "$0")"; mkdir -p out
export N8N_USER_FOLDER="$(pwd)/.n8n-home" N8N_RESTRICT_FILE_ACCESS_TO="$(cd .. && pwd)" N8N_DIAGNOSTICS_ENABLED=false N8N_VERSION_NOTIFICATIONS_ENABLED=false N8N_RUNNERS_ENABLED=true
npx -y n8n@2.48.7 import:workflow --input=workflow.json
npx -y n8n@2.48.7 execute --id colisRetard01
