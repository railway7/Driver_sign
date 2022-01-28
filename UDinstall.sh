#!/usr/bin/env bash
sudo -i
sudo wget -N http://chromedriver.storage.googleapis.com/97.0.4692.20/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
sudo apt install -f -y
sudo python3 -V
sudo apt --fix-broken install -y
sudo apt-get install -y python3-pip -y
sudo wget https://npm.taobao.org/mirrors/chromedriver/97.0.4692.71/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo ln -sf /chromedriver /usr/bin/chromedriver
sudo apt install chromium-driver -y
sudo apt-get update -y
sudo apt-get install xvfb -y
sudo wget https://raw.githubusercontent.com/spiritLHL/Gecko_sign/master/requirements.txt
sudo pip3 install -r requirements.txt
