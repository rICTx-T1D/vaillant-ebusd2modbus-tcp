# MQTT2Fronius-SM-modbusTCP

🧠 Dieses Projekt emuliert ein dreiphasigen Smartmeter um diesen an GEN24 anzubinden

## 🚀 Schnellstart

### 1. Voraussetzungen

- Docker
- MQTT-Broker
- Wechselrichter Fronius GEN24 oder technisch baugleich

### 2. Konfiguration in docker-compose.yml

```bash
      - PYTHONUNBUFFERED=1
      - LOG_LEVEL=DEBUG
      - MODBUS_PORT=1502
      - MQTT_BROKER_HOST=mqttbroker.internal
      - MQTT_BROKER_PORT=1883
      - MQTT_BROKER_USERNAME=mqttuser
      - MQTT_BROKER_PASSWORD=mqttpassword
      - MQTT_TOPIC_CURRENT_POWER=FroniusSM/01/power_W
      - MQTT_TOPIC_TOTAL_IMPORT=FroniusSM/01/import_total_kWh
      - MQTT_TOPIC_TOTAL_EXPORT=FroniusSM/01/export_total_kWh
```
### 3. Wechselrichter Konfiguration 
- Anmelden als technican-User
- Gerätekonfiguration -> Komponenten -> Komponente hinzufügen -> Zähler
- Typ: Fronius Smart Meter (Modbus TCP)
- Anwendung: Erzeugungszähler (für PV) oder Verbrauchszähler
- Name: [beliebig]
- Kategorie: [beliebig, siehe Auswahl-Box]
- IP-Adresse: IP des Hosts, auf dem Docker läuft und der Container bereitgestellt wird
- Port:  1502    (502 oder 1502 mehr kann der WR nicht - tcp/502 braucht Container mit root)
- Modbus-Adresse:  100 + x (wenn mehrere Zähler darf jede Modbus-Adresse nur einmal vergeben werden --> 1=WR, 2=Akku)
