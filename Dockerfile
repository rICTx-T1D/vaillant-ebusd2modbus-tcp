FROM python:3.11-alpine
RUN pip install pymodbus
COPY ebus2modbus.py /app/ebus2modbus.py
WORKDIR /app
CMD ["python", "ebus2modbus.py"]