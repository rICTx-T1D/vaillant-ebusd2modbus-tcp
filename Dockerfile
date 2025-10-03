FROM python:3.11-alpine

# Installiere Abhängigkeiten
RUN pip install --no-cache-dir pymodbus==3.11.3

# Kopiere das Python-Skript
COPY ebus2modbus.py /app/ebus2modbus.py

# Setze Arbeitsverzeichnis
WORKDIR /app

# Starte das Skript
CMD ["python", "ebus2modbus.py"]
