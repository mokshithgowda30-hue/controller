import serial
import pydirectinput
import time

# -----------------------
COM_PORT = 'COM7'
BAUD_RATE = 9600
# -----------------------

print("Connecting to Arduino...")

try:
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    ser.reset_input_buffer()   # Clear any garbage data
    print("Connected! Ready to play.")
except Exception as e:
    print(f"Error: {e}")
    exit()

current = "CENTER"

try:
    while True:
        if ser.in_waiting > 0:

            # Read serial data safely
            command = ser.readline().decode('utf-8', errors='ignore').strip()

            # Uncomment this line if you want to see what Arduino is sending
            # print(command)

            if command == "STEER_LEFT":
                if current != "LEFT":
                    pydirectinput.keyUp('d')
                    pydirectinput.keyDown('a')
                    current = "LEFT"

            elif command == "STEER_RIGHT":
                if current != "RIGHT":
                    pydirectinput.keyUp('a')
                    pydirectinput.keyDown('d')
                    current = "RIGHT"

            elif command == "STEER_CENTER":
                if current != "CENTER":
                    pydirectinput.keyUp('a')
                    pydirectinput.keyUp('d')
                    current = "CENTER"

except KeyboardInterrupt:
    print("Stopping...")

finally:
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('d')
    ser.close()