#!/usr/bin/env bash

set -e

ROOTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

wget -q --tries=2 --timeout=100 http://www.google.com.com -O /dev/null
if [ $? -eq 0 ];then
	echo "Connected"
else
	echo "Unable to Connect, try again !!!"
	exit 0
fi

if [ -d "$HOME/BakeBit" ]; then
    sudo rm -rf $HOME/BakeBit
fi

echo $ROOTDIR
sudo apt-get update
sudo apt-get install -y avrdude
sudo apt-get install -y python-requests
sudo apt-get install -y nodejs
sudo apt-get install -y npm

sudo ln -s "$(which nodejs)" /usr/bin/node
sudo cp $ROOTDIR/avrdude.conf /etc

cd $ROOTDIR/server
npm install

cd $HOME
git clone https://github.com/grassjelly/BakeBit

cd $HOME/BakeBit/Firmware
sudo ./firmware_update.sh 

cd $HOME/BakeBit/Script/
sudo ./install.sh
