#!/bin/bash

sudo apt install python3 python3-dev python3-pip 
# matplotlib dependencies
sudo apt install libpng-dev libjpeg8-dev libfreetype6-dev
# upgrade pip3
sudo -H pip3 install --upgrade pip
# install pyzmq
sudo -H pip3 install --upgrade zmq
# install ipython3, jupyter
sudo apt install ipython3
sudo -H pip3 install --upgrade jupyter
# minimal installation : jupyter[notebook]

# install python3 kernel for notebook
sudo ipython3 kernel install

# install jupyter themes
sudo -H pip3 install jupyterthemes

# set theme
sudo jt -t grade3

# open up jupyter notebook
jupyter notebook

# open notebook and check for python3 kernel
#		$ jupyter notebook
# firefox http://i.stack.imgur.com/TF5uW.png

# install virtual env
sudo -H pip3 install --upgrade virtualenv
