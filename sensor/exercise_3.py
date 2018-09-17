import time
import bakebit
import requests

URL = 'http://localhost:8000/sensors'
 
# Connect the BakeBit Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0
 
# Connect the LED to digital port D5
# SIG,NC,VCC,GND
led = 5

lowThreshold = 700
highTreshold = 1023

bakebit.pinMode(light_sensor,"INPUT")
bakebit.pinMode(led,"OUTPUT")
time.sleep(1)
 
# Reference voltage of ADC is 5v
adc_ref = 5

def send_to_server(type, value):
    try:
        payload = {"sensors": type, "value": value}
        print payload
        r = requests.post(URL, data=payload)
        print r.text
    except:
        print("Server Down")


while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = bakebit.analogRead(light_sensor)

        send_to_server("lux", sensor_value)
 
        # Calculate voltage
        voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
 
        # Calculate LED brightess (0 to 255)
        if sensor_value > lowThreshold:
            brightness = int(((float)(sensor_value) - lowThreshold) / (highTreshold - lowThreshold) * 255)
        elif sensor_value > highTreshold:
            brightness = 255
        else:
            brightness = 0
 
        # Give PWM output to LED
        bakebit.analogWrite(led,brightness)
 
        print("sensor_value = %d voltage = %.2f brightness = %d" %(sensor_value, voltage, brightness))
    except KeyboardInterrupt:
        bakebit.analogWrite(led,0)
        break
    except IOError:
        print ("Error")
