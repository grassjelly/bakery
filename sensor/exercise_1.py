﻿import time
import bakebit
 
# Connect the BakeBit Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
potentiometer = 0
 
# Connect the LED to digital port D5
# SIG,NC,VCC,GND
led = 5
 
bakebit.pinMode(potentiometer,"INPUT")
bakebit.pinMode(led,"OUTPUT")
time.sleep(1)
 
# Reference voltage of ADC is 5v
adc_ref = 5
 
# Vcc of the BakeBit interface is normally 5v
bakebit_vcc = 5
 
# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300
 
while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = bakebit.analogRead(potentiometer)
 
        # Calculate voltage
        voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
 
        # Calculate rotation in degrees (0 to 300)
        degrees = round((voltage * full_angle) / bakebit_vcc, 2)
 
        # Calculate LED brightess (0 to 255) from degrees (0 to 300)
        brightness = int(degrees / full_angle * 255)
 
        # Give PWM output to LED
        bakebit.analogWrite(led,brightness)
 
        print("sensor_value = %d voltage = %.2f degrees = %.1f brightness = %d" %(sensor_value, voltage, degrees, brightness))
    except KeyboardInterrupt:
        bakebit.analogWrite(led,0)
        break
    except IOError:
        print ("Error")