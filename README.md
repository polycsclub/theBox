# The Box

![Model in Fusion 360](https://raw.githubusercontent.com/sciencedude100/theBox/master/model.png)

## Parts
* Raspberry Pi
* Camera
* Power of some sort
* LED

## Software
* Python
* [Amazon Rekognition](https://github.com/boto/boto3#quick-start)

## [Cost:](https://aws.amazon.com/rekognition/pricing/)
### Live Video
* `$0.12` per minute of live video
* `44,640` minutes per month
* **$5,356.80** per full month of usage

### One Frame Per 3 Seconds
* `$1.00` per million images
* `44,640` minutes per month
* `20` images per minute
* `892,800` images per month
* **$1.00** per full month of usage

## Logic Plan
* pull frame from camera
* push frame to AWS
* parse response
* does the response contain ~~"Cat"~~ "Human"
  * is the confidence over 60%
    * turn light on
  * no, turn the light off
* no, turn the light off

### Changes to Original Plan
* change from recognizing cats to people, as I don't have a cat
* ~~change from lighting an LED to making a sound, as I can't find an LED and it's 3AM~~ bought some LEDs

## Usage
1. Install Dependencies with `install-requirements.sh`
2. Follow Instructions [here](https://github.com/boto/boto3#quick-start) to create AWS config files for Boto3
3. Run Programs with `./detect.py <URL OF IMAGE>` or `./recognize.py`

## [`detect.py` Demo](https://www.youtube.com/watch?v=Vzd3liGFyoU):
[![TheBox Demo](https://img.youtube.com/vi/Vzd3liGFyoU/0.jpg)](https://www.youtube.com/watch?v=Vzd3liGFyoU)
