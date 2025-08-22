#!/bin/bash

# --- Tu Motor de Contenido Diario v0.2 ---

echo "⚙️  Generando tweet del día..."

# 1. Ejecuta el script de Python para generar el tweet y lo guarda en una variable
TWEET_GENERATED=$(python engine.py)

# muestra el tweet en el terminal
echo "--- 🐦 TWEET GENERADO ---"
echo "$TWEET_GENERATED"
echo "-------------------------------------"


echo "💾  Archivando log en el registro semanal..."

# 2. Archiva el log.txt en weekly_log.md con fecha y un separador y el tweet generado en weekly_log.md
FECHA_ACTUAL=$(date +%Y-%m-%d)
echo "## 🪵  LOG: $FECHA_ACTUAL" >> weekly_log.md
cat log.txt >> weekly_log.md
echo "" >> weekly_log.md
echo "### 🐦 Tweet Publicado:" >> weekly_log.md
echo "> $TWEET_GENERADO" >> weekly_log.md # Usamos '>' para formato de cita en Markdown
echo "" >> weekly_log.md
echo "---" >> weekly_log.md

echo "✅  ¡Listo! Tu tweet está generado y todo ha sido archivado."