#controlling car motors in ssh 
python3 - <<'PY'
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)

commands = [
    ("FORWARD", b"F,100\n"),
    ("STOP",    b"STOP\n"),
    ("BACKWARD",b"B,100\n"),
    ("STOP",    b"STOP\n"),
    ("LEFT",    b"L,100\n"),
    ("STOP",    b"STOP\n"),
    ("RIGHT",   b"R,100\n"),
    ("STOP",    b"STOP\n"),
]

for name, cmd in commands:
    print("Sending:", name)
    ser.write(cmd)
    time.sleep(1)

ser.close()
PY
