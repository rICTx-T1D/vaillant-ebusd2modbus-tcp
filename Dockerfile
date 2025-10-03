# Minimaler Alpine-Basiscontainer mit Python
FROM python:3.11-alpine

# Installiere benötigte Pakete
RUN pip install pymodbus

# Kopiere das Python-Skript in den Container
COPY ebus2modbus.py /app/ebus2modbus.py

# Setze Arbeitsverzeichnis
WORKDIR /app

# Starte das Skript
CMD ["python", "ebus2modbus.py"]