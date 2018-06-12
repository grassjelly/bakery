#!/usr/bin/env python

import time
import bakebit
import requests

URL = 'http://localhost:8000/sensors'

# Connect the BakeBit Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the BakeBit LED Bar to digital port D3
# DI,DCKI,VCC,GND
ledbar = 3

lowThreshold = 500
highTreshold = 600

bakebit.pinMode(light_sensor,"INPUT")
bakebit.pinMode(ledbar,"OUTPUT")
time.sleep(.2)
bakebit.bakeBitLedBar_Init(ledbar, 0, 5)
time.sleep(.5)
old_color = 0

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
        light_count = 0
        
        # Get sensor value
        sensor_value = bakebit.analogRead(light_sensor)

        send_to_server("lux", sensor_value)

        if sensor_value > highTreshold:
            f=(1023-highTreshold)/4
            light_count =  (sensor_value-highTreshold)/f+1
            
            # turn on ledbar
            color16bit = bakebit.Green
            if light_count > 1:
                color16bit = color16bit | (bakebit.Green << 3)
            if light_count > 2:
                color16bit = color16bit | (bakebit.Green << 6)
            if light_count > 3:
                color16bit = color16bit | (bakebit.Green << 9)
            if light_count > 4:
                color16bit = 0
                color16bit = color16bit | bakebit.Blue
                color16bit = color16bit | (bakebit.Blue << 3)
                color16bit = color16bit | (bakebit.Blue << 6)
                color16bit = color16bit | (bakebit.Blue << 9)
                color16bit = color16bit | (bakebit.Blue << 12)
            
            if color16bit != old_color:
                old_color = color16bit
                lowBits = color16bit & 255
                highBits = (color16bit & (255 << 8)) >> 8
                bakebit.bakeBitLedBar_Show(ledbar, highBits, lowBits)

        elif sensor_value < lowThreshold:
            # turn off ledbar
            bakebit.bakeBitLedBar_Show(ledbar, 0, 0)
            
            print("sensor_value = %d light_count =%d" %(sensor_value,  light_count))
            time.sleep(.5)

    except KeyboardInterrupt:
        bakebit.bakeBitLedBar_Release(ledbar)
        time.sleep(.2)
        break
    except IOError:
        print ("Error")

    time.sleep(1)

