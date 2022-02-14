#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo update-locale LANG=en_US.UTF-8 LANGUAGE=en.UTF-8
# echo 'export export LC_ALL=C' >> /home/vagrant/.profile

# install python versions
# sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt-get update
# sudo apt-get install -y python3.6-dev
# sudo apt-get install -y python3.7-dev
# sudo apt-get install -y python3.8-dev
# sudo apt-get install -y python3-distutils
# sudo apt-get install -y python3.9-dev
# sudo apt-get install -y python3.9-distutils
# sudo apt-get install -y python3.10-dev
# sudo apt-get install -y python3.10-distutils

# tools
sudo apt-get install -y mc xvfb x11-utils scrot
sudo apt-get install -y python3-pip

# project dependencies
sudo apt-get install -y zenity
sudo apt-get install -y gxmessage

# sudo apt-get install -y python-gi
sudo apt-get install -y python3-gi
sudo apt-get install -y gir1.2-gtk-3.0

sudo apt-get install -y python3-wxgtk4.0
sudo apt-get install -y python3-pyqt5
sudo apt-get install -y python3-dialog
sudo apt-get install -y python3-easygui
sudo pip3 install -U easygui

sudo apt-get install -y python3-pyside2.qtwidgets
#sudo pip3 install pyside2 --no-cache-dir

# test dependencies
#  sudo apt-get install -y x11-utils #   for: xmessage
#  sudo apt-get install -y x11-apps  #   for: xlogo
sudo python3 -m pip install tox

