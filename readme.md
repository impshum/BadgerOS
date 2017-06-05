# Such Badger OS

*A very stranger way to take pictures of people (and things).*



## Pinky

###### Equipment

* Raspberry Pi 2 B+
* Pi Camera v2
* TP-Link mini WiFi router
* Surveillance/CCTV style case and mount
* 1 x CAT5 cable
* 1 x 16Gb SD card
* 1 x 5V 1.5A power

###### Operating System

* motionyeos - https://github.com/ccrisan/motioneyeos/wiki
* Python 2.7

###### Processes

* Streams a continuous view of camera input.
* Keeps 3 frames before and after movement in a specified area/mask for 1 day.
* Responds to commands from Brain.
* Doesn't like posers!



## Brain

###### Equipment

* Raspberry Pi 3 B+
* GERT VGA666
* 1 x Projector
* 1 x HD Monitor
* 1 x HDMI cable
* 1 x 32Gb SD card
* 1 x 5V 2.5A power

###### Operating System

* Raspbian Jessie (April 2017) - https://www.raspberrypi.org/downloads/raspbian/
* OpenCV 3.1.0
* Python 2.7

###### Processes

* Ask Pinky if there are new images to process.
* If there is new images the following functions are fired...
  * SSH into Pinky.
    * Create new gallery folder based on date and time.
    * Move new images into new gallery folder.
    * Rename new images numerically.
    * Move new gallery folder over to Brain.
  * Exit Pinky with style.
  * Remove images that don't contain quality pictures of human faces.
  * Complain about pictures that contain cats.
  * Love Plank!
  * SSH into Rocket.
    * Move new gallery folder to collection.
    * Update daily collection slideshow.
    * Move new gallery folder to remote server.
* If there is no new images to process.
  * Continue displaying all the things and wait for new images.




## Rocket

###### Equipment

* Raspberry Zero W
* 1 x 4Gb SD card
* 1 x 5V 1.5A power

###### Operating System

* Raspbian Jessie Lite (April 2017) - https://www.raspberrypi.org/downloads/raspbian/
* Python
* Bash

###### Processes

* Runs a local nginx server with daily photo galleries.
* Responds to commands from Brain.
* Uploads pictures to remote server.



## The Scientist

###### Equipment

* VPS

###### Operating System

* CentOS - https://www.centos.org
* Python 2.7
* Other sparkly stuff

###### Processes

* Runs a public nginx server with full photo galleries.
* Responds to commands from Brain.
* Tweets random images when activity is heavy.



*STILL UNDER HEAVENLY DEVELOPMENT DUE TO THE LACK OF BADGERS*

*MORE TO COME OVER THE NEXT WEEK*
