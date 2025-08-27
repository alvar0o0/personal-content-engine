#!/bin/bash

# --- Tu Motor de Contenido Diario v0.5 ---
TWEET_GENERADO=$(python3 engine.py)

if [ -z "$TWEET_GENERADO" ]; then
  echo "⚠️  el scrip de python generó ningún tweet. no se archivará nada"
  exit 1
fi

echo "--- TWEET GENERADO---"
echo "$TWEET_GENERADO"
echo "----------------------"

echo "archivando en el registro semanal..."
FECHA_ACTUAL=$(date +%Y-%m-%d)
echo "## LOG: $FECHA_ACTUAL" >> weekly_log.md
cat log.txt >> weekly_log.md
echo "TWEET PUBLICADO:" >> weekly_log.md
echo "$TWEET_GENERADO" | sed 's/^/> /' >> weekly_log.md
echo "" >> weekly_log.md
echo "---" >> weekly_log.md

echo "-PROCESO COMPLETO-"
