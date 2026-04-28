import numpy as np
import serial
from serial.tools import list_ports
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# ----------------------------
# SERIAL CONNECTION
# ----------------------------
ser = None
try:
    ser = serial.Serial('COM5', 9600)
    print("Connected to COM5")
except:
    print("Arduino not found → DEMO MODE")
    ports = [p.device for p in list_ports.comports()]
    print("Available ports:", ports)
    ser = None

# ----------------------------
# SIMPLE RANGE-BASED CLASSIFIER (using MAX)
# ----------------------------
def classify_activity(max_val):
    if max_val <= 1:
        return "Standing"
    elif max_val <= 3:
        return "Walking"
    elif max_val <= 5:
        return "Running"
    else:
        return "Jumping"

# ----------------------------
# GRAPH SETUP
# ----------------------------
plt.style.use('ggplot')
fig, ax = plt.subplots()

x_data = list(range(20))
y_data = [0] * 20

line, = ax.plot(x_data, y_data, lw=2)
text_activity = ax.text(0.5, 1.05, "", transform=ax.transAxes,
                        ha="center", fontsize=14)

ax.set_ylim(0, 10)
ax.set_title("Piezo Activity Recognition")
ax.set_xlabel("Sample")
ax.set_ylabel("Sensor Value")

# ----------------------------
# GET DATA
# ----------------------------
def get_activity_data():
    data = []

    if ser is None:
        # Demo values for small 0–8 piezo range
        activity = random.choice(["Standing", "Walking", "Running", "Jumping"])

        if activity == "Standing":
            data = [random.randint(0, 1) for _ in range(20)]
        elif activity == "Walking":
            data = [random.randint(2, 3) for _ in range(20)]
        elif activity == "Running":
            data = [random.randint(4, 5) for _ in range(20)]
        elif activity == "Jumping":
            data = [random.randint(6, 8) for _ in range(20)]

        print(f"DEMO MODE → Simulating: {activity}")
        return data

    # REAL ARDUINO MODE
    while len(data) < 20:
        try:
            value = int(ser.readline().decode().strip())
            data.append(value)
        except:
            pass

    return data

# ----------------------------
# UPDATE LOOP
# ----------------------------
def update(frame):
    data = get_activity_data()

    max_value = np.max(data)
    predicted = classify_activity(max_value)

    line.set_ydata(data)
    text_activity.set_text(f"Predicted: {predicted}")

    return line, text_activity

# ----------------------------
# RUN
# ----------------------------
ani = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
plt.show()