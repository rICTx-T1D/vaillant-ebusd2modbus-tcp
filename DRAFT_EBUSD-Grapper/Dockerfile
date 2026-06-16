FROM python:3.11-alpine

# Systempakete für pip-Upgrade und saubere Builds
RUN apk add --no-cache gcc musl-dev libffi-dev

# Upgrade pip auf neueste Version
RUN pip install --no-cache-dir --upgrade pip

# Installiere pymodbus in aktueller Version
RUN pip install --no-cache-dir pymodbus==3.11.3

# Kopiere das Python-Skript
COPY ebus2modbus.py /app/ebus2modbus.py

# Setze Arbeitsverzeichnis
WORKDIR /app

# Starte das Skript
CMD ["python", "ebus2modbus.py"]
