# The Box

## Parts
* Raspberry Pi
* Camera
* Power of some sort

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
* does the response contain "cat"
  * is the confidence over 60%
    * turn light on
  * no, turn the light off
* no, turn the light off
