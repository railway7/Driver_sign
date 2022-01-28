#!/usr/bin/env bash
sudo -i
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get upgrade -y
sudo apt-get update -y
sudo apt-get -f install -y
dpkg -i google-chrome-stable_current_amd64.deb -y
sudo apt install -f -y
python3 -V
apt --fix-broken install -y
sudo apt-get install -y python3-pip -y
wget https://npm.taobao.org/mirrors/chromedriver/97.0.4692.71/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
ln -sf /chromedriver /usr/bin/chromedriver
sudo apt install chromium-driver -y
sudo apt-get update -y
sudo apt-get install xvfb -y
wget https://raw.githubusercontent.com/spiritLHL/Gecko_sign/master/requirements.txt
pip3 install -r requirements.txt
