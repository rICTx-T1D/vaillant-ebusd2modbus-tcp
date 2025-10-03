import os, socket, time, threading
from pymodbus.server import ModbusTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSequentialDataBlock
from pymodbus.datastore.store import BaseModbusDataBlock

# Modbus TCP Port (default: 502)
MODBUS_PORT = int(os.getenv("MODBUS_PORT", "502"))

# ebusd TCP Host/Port (default: 127.0.0.1:8888)
EBUSD_HOST = os.getenv("EBUSD_HOST", "127.0.0.1")
EBUSD_PORT = int(os.getenv("EBUSD_PORT", "8888"))

# Holding Register 0 = VerbrauchWP
block = ModbusSequentialDataBlock(0, [0])
store = {
    "hr": block  # Holding Register
}
context = ModbusServerContext(slaves=store, single=True)

# Datenpunkte, die summiert werden sollen
data_points = [
    "CurrentConsumedPower",
    "BuildingCircuitPumpPowerSensor",
    "ImmersionHeaterPower"
]

def ebus_read(dp):
    try:
        with socket.create_connection((EBUSD_HOST, EBUSD_PORT), timeout=5) as s:
            s.sendall(f"read -m 10 {dp}\n".encode())
            response = s.recv(128).decode().strip()
            return float(response.split('=')[-1])
    except Exception as e:
        print(f"Fehler bei {dp}: {e}")
        return 0.0

def update_register():
    while True:
        verbrauch_wp = sum(ebus_read(dp) for dp in data_points)
        context.setValues("hr", 0, [int(verbrauch_wp)])
        print(f"VerbrauchWP: {int(verbrauch_wp)} W")
        time.sleep(10)

threading.Thread(target=update_register, daemon=True).start()
ModbusTcpServer(context, address=("0.0.0.0", MODBUS_PORT)).serve_forever()
