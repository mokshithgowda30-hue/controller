python3 - <<'PY'
import serial
import time

PORT = "/dev/ttyUSB1"

ser = serial.Serial(
    PORT,
    115200,
    timeout=1,
    dsrdtr=False,
    rtscts=False
)

ser.dtr = False
ser.rts = False

print("LiDAR connected")
print("Motor should be spinning...")

# Clear anything old
ser.reset_input_buffer()

# Send START SCAN
ser.write(bytes([0xA5, 0x20]))
ser.flush()

print("START SCAN sent")
time.sleep(1)

print("Collecting data for 10 seconds...")
print()

start = time.time()
total = 0

try:
    while time.time() - start < 10:
        data = ser.read(512)

        if data:
            total += len(data)
            print(f"Received {len(data)} bytes")
            print(data.hex(" "))
        else:
            print("NO DATA")

except KeyboardInterrupt:
    pass

print()
print("Total bytes received:", total)

# Stop scan
ser.write(bytes([0xA5, 0x25]))
ser.flush()

time.sleep(0.5)
ser.close()

print("Done.")
PY
