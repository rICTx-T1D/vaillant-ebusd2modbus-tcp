import os, socket, time, threading
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Modbus-Port aus Umgebungsvariable (Standard: 502)
MODBUS_PORT = int(os.getenv("MODBUS_PORT", "502"))

# Modbus Holding Register: Register 0 = VerbrauchWP
store = ModbusSlaveContext(hr={0: 0})
context = ModbusServerContext(slaves=store, single=True)

# Datenpunkte, die summiert werden sollen
data_points = [
    "CurrentConsumedPower",
    "BuildingCircuitPumpPowerSensor",
    "ImmersionHeaterPower"
]

def ebus_read(dp):
    try:
        with socket.create_connection(("127.0.0.1", 8888), timeout=5) as s:
            s.sendall(f"read -m 10 {dp}\n".encode())
            response = s.recv(128).decode().strip()
            return float(response.split('=')[-1])
    except Exception as e:
        print(f"Fehler bei {dp}: {e}")
        return 0.0

def update_register():
    while True:
        verbrauch_wp = sum(ebus_read(dp) for dp in data_points)
        context[0].setValues(3, 0, [int(verbrauch_wp)])
        print(f"VerbrauchWP: {int(verbrauch_wp)} W")
        time.sleep(10)

threading.Thread(target=update_register).start()
StartTcpServer(context, address=("0.0.0.0", MODBUS_PORT))