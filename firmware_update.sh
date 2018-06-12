#!/usr/bin/env bash

set -e

ROOTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $HOME/BakeBit/Firmware 
sudo ./firmware_update.sh  
sleep 2 
i2cdetect -y 0