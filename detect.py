#!/usr/bin/python

# This script is to demo the AWS Boto3 Library with Rekognition

import boto3
import requests
import sys

if len(sys.argv) < 2 :
    print("Usage: ./detect.py <URL OF IMAGE>")
    exit()

valid = False
threshold = 70
session = boto3.Session(profile_name="default")
rekognition = session.client("rekognition")
result = requests.get(sys.argv[1])
result_content = result.content
rekognition_result = rekognition.detect_labels(Image={"Bytes":result_content}, MaxLabels=16, MinConfidence=70)
for instance in rekognition_result["Labels"]:
    print(str(instance["Name"]) + " : " + str(instance["Confidence"]))
    if str(instance["Name"]) == "Cat" and instance["Confidence"] >= threshold :
        print("Valid CAT");
        valid = True

if valid :
    print("+--------------+")
    print("|              |")
    print("| Found a cat! |")
    print("|              |")
    print("+--------------+")
