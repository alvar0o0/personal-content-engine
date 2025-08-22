#!/bin/bash

# --- Tu Motor de Contenido Diario v0.2 ---

echo "⚙️  Generando tweet del día..."

# 1. Ejecuta el script de Python para generar el tweet
#    La salida se mostrará en la terminal para que la copies.
python engine.py

echo "-------------------------------------"
echo "💾  Archivando log en el registro semanal..."

# 2. Archiva el log.txt en weekly_log.md con fecha y un separador
#    - Obtiene la fecha actual en formato YYYY-MM-DD
#    - Añade la fecha y un separador a weekly_log.md
#    - Añade el contenido de tu log.txt a weekly_log.md

FECHA_ACTUAL=$(date +%Y-%m-%d)
echo "## 🪵  LOG: $FECHA_ACTUAL" >> weekly_log.md
cat log.txt >> weekly_log.md
echo "" >> weekly_log.md # Añade un espacio para el siguiente log
echo "---" >> weekly_log.md # Añade una línea separadora

# 3. (Opcional) Limpia el log.txt para el día siguiente
> log.txt

echo "✅  ¡Listo! Tu tweet está generado y el log del día ha sido archivado."