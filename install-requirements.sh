#!/bin/bash

# This script installs the packages python-pip, python-opencv, and ffmpeg
# It also uses pip to install requests and boto3

sudo apt-get install python-pip python-opencv ffmpeg -y

sudo pip install requests boto3
