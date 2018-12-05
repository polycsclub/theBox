#!/usr/bin/python

import boto3
import requests
from subprocess import call
import cv2
import base64
import RPi.GPIO as GPIO

threshold = 70		# set the threshold percentage to accept
object = "Human"	# set the object name to be recognized
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)


# Open Rekognition Session
session = boto3.Session(profile_name="default")
rekognition = session.client("rekognition")

while True :
# Pull image from camera
capture = cv2.VideoCapture(0)
return_value, image = capture.read()
capture.release()
return_value, buffer = cv2.imencode(".jpg", image)

# Because of odd things with base64 and image encoding, I have to save the image to disk
#    then read it back for Boto3 library
with open("Last.jpg", "wb") as f :
    f.write(buffer)


with open("Last.jpg", "rb") as f :
    rekognition_result = rekognition.detect_labels(Image={"Bytes":f.read()}, MaxLabels=16, MinConfidence=70)	# Submit Rekognition request

# Parse Rekognition result
for instance in rekognition_result["Labels"]:
    print(str(instance["Name"]) + " : " + str(instance["Confidence"]))
    if str(instance["Name"]) == object and instance["Confidence"] >= threshold :
        print("Valid " + object);
        GPIO.output(26, GPIO.HIGH)
    else:
        GPIO.output(26, GPIO.LOW)

GPIO.cleanup([26, 20, 21])
