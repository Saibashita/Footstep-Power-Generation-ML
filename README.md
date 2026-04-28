# ⚡ Footstep Power Generation & Activity Detection using Piezo Sensors

## 📌 Overview

This project focuses on generating electrical energy using piezoelectric sensors and detecting human activities using Machine Learning.

It converts mechanical energy (footsteps) into electrical signals and classifies activities like:

* Walking
* Running
* Jumping
* Standing

## 🧠 Key Features

* Energy harvesting using piezo sensors
* Arduino-based real-time data acquisition
* Signal processing and feature extraction
* Machine Learning classification (Random Forest)
* Real-time visualization

## 🏗️ System Architecture

* Piezo sensor array
* Arduino Uno
* Signal conditioning circuit
* Serial communication
* Python ML model

## ⚙️ Working Principle

* Piezo sensors generate voltage when pressure is applied
* AC signal → Rectified → Filtered → Stored
* Arduino reads values and sends to PC
* ML model classifies activity

## 📊 Features Used

* Amplitude
* Energy
* Standard Deviation
* Peak Count
* Zero Crossing Rate

## 🤖 Machine Learning Model

* Algorithm: Random Forest
* Activities classified:

  * Standing → Near zero signal
  * Walking → Periodic spikes
  * Running → High frequency spikes
  * Jumping → High amplitude spikes

## 📁 Dataset

Collected using Arduino and stored as:

* walking.txt
* running.txt
* jumping.txt
* standing.txt



🔌 Communication Protocols Used

This project uses two different communication protocols for efficient data transfer and display:

1️⃣ UART (Serial Communication)
Used for communication between Arduino and Computer
Transfers real-time sensor data from piezo sensors to the Python-based machine learning model
Implemented using Arduino’s built-in serial interface
Example: Serial.println(sensorValue);

2️⃣ I²C (Inter-Integrated Circuit)
Used for interfacing the 16x2 LCD display with Arduino
Requires only two communication lines:
SDA (Data line)
SCL (Clock line)
Example:
Arduino acts as Master
LCD acts as Slave (address: 0x27)
LiquidCrystal_I2C lcd(0x27, 16, 2);

🔄 Overall Communication Flow
Piezo Sensors → Arduino (Analog Input)
        ↓
   UART Communication
        ↓
   Computer (Python ML Model)

AND

Arduino → I²C → LCD Display

## ▶️ How to Run

```bash
pip install -r requirements.txt
python train_model.py
python predict.py
```

## 🧪 Results

* Successfully classified human activities
* Generated usable electrical energy
* Real-time graphs visualized

## ⚠️ Challenges

* Noise in signals
* Low sensitivity
* Requires high pressure

## 🌍 Applications

* Smart floors
* Energy harvesting in public spaces
* Fitness tracking
* Security systems


