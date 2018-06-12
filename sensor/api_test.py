#!/usr/bin/python

import time
import requests
import random

URL = 'http://localhost:8000/sensors'

def send_to_server(type, value):
    try:
        payload = {"sensors": type, "value": value}
        print payload
        r = requests.post(URL, data=payload)
        print r.text
    except:
        print("Server Down")

def get_sensor_reading():
    return random.randint(1,101)

def main():
    while True:
        send_to_server("sound", get_sensor_reading())
        time.sleep(1)

if __name__ == "__main__":
    main()