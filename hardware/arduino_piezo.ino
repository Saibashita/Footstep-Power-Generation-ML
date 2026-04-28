#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Pins
int piezoPin = A0;
int ledPin = 8;   // transistor base connected here

// Variables
int threshold = 5;
int stepCount = 0;
bool stepDetected = false;

void setup() {
  lcd.init();
  lcd.backlight();

  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);

  lcd.setCursor(0, 0);
  lcd.print("Piezo System");
  delay(2000);
  lcd.clear();
}

void loop() {

  int sensorValue = analogRead(piezoPin);

  // Convert to voltage
  float voltage = sensorValue * (5.0 / 1023.0);

  Serial.print("Value: ");
  Serial.print(sensorValue);
  Serial.print("  Voltage: ");
  Serial.println(voltage);

  // STEP DETECTION
  if (sensorValue > threshold && !stepDetected) {
    stepCount++;
    stepDetected = true;

    // LED ON
    digitalWrite(ledPin, HIGH);

    delay(150);   // hold LED + avoid multiple counts
  }

  // Reset detection
  if (sensorValue < threshold) {
    stepDetected = false;
    digitalWrite(ledPin, LOW);  // LED OFF
  }

  // LCD Display
  lcd.setCursor(0, 0);
  lcd.print("Steps: ");
  lcd.print(stepCount);
  lcd.print("   ");

  lcd.setCursor(0, 1);
  lcd.print("V:");
  lcd.print(voltage, 2);
  lcd.print(" ");

  delay(50);
}