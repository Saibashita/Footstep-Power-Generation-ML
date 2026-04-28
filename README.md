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


