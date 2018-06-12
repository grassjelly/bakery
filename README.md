## Installing project dependencies
This will install all software packages and drivers required to run the applications found in this project:

    ./setup.sh

Once the pi has rebooted, install the Baketbit python library:

    cd $HOME/BakeBit/Software/Python/
    sudo python setup.py install

## Updating the firmware
Bakebit hats running on Atmel 328PB doesn't seem to be detected on i2c bus, so firmware update is required. Run:

    ./firmware_update.sh

## Running the dashboard

    cd server
    node server.js

## Running the sensor node

    cd sensor
    python exercise_2.py
