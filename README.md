# vaillant-ebusd2modbus-tcp
convert vwl 75/5 power data over ebusd to modbus-tcp to fronius gen 24



# ebus2modbus

🧠 Brücke zwischen `ebusd` und Modbus TCP – ideal für Fronius GEN24, Home Assistant oder andere Modbus-Clients.

## 🔧 Projektbeschreibung

Dieses Projekt stellt eine schlanke Modbus-TCP-Bridge bereit, die Verbrauchswerte aus `ebusd` ausliest und als Modbus-Holding-Register bereitstellt. Damit kann z. B. ein Fronius GEN24 Wechselrichter den Stromverbrauch der Wärmepumpe erfassen.

## 📦 Features

- Liest definierte Power-Datenpunkte aus `ebusd` via TCP (`127.0.0.1:8888`)
- Summiert die Werte zu einem Gesamtverbrauch (`VerbrauchWP`)
- Stellt diesen Wert über Modbus TCP im Holding Register `0` bereit
- Minimaler Docker-Container auf Alpine-Basis mit Python

## 🚀 Schnellstart

### 1. Voraussetzungen

- `ebusd` läuft im Docker mit `--network host` und aktiviertem TCP (`--enable-tcp --port=8888`)
- Python 3.11 oder Docker

### 2. Build mit Docker

```bash
git clone https://github.com/rICTx-T1D/vaillant-ebusd2modbus-tcp.git
cd ebus2modbus
docker build -t ebus2modbus .
docker run --network host \
  -e MODBUS_PORT=1502 \
  -e EBUSD_HOST=127.0.0.1 \
  -e EBUSD_PORT=8888 \
  ebus2modbus
# ^^ modbus port tcp/502 need root, use 1502 for rootless 