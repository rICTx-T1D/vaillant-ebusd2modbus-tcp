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