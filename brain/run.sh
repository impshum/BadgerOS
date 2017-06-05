#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

cd ~/

if [ -z "$(ls -A /home/pi/Brain/uploaded/ready/)" ]; then
  printf "${RED}No new pictures to process\n${NC}"
else
  printf "${GREEN}Found new pictures to process\n${NC}"

  # RUN OPENCV ON UPLOADED FOLDER
  python /home/pi/Brain/py/start.py
  find /home/pi/Brain/uploaded/ready/ -name "*.jpg" -exec python /home/pi/Brain/py/detect.py {} \;
  python /home/pi/Brain/py/results.py

  echo "Creating gallery folder"

  cd /home/pi/Brain/ready/

  mkdir $(date '+%d-%b-%Y-%H:%M');

  shifty="$(ls -ltr |grep ^d |tail -1 | awk '{print $9}')"

  cd $shifty

  echo "Moving pictures"

  find /home/pi/Brain/uploaded/ready/ -mindepth 2 -type f -print -exec mv {} $shifty \;

  #cp -r /home/pi/Brain/gallery/* .

  #rm -r /home/pi/Brain/gallery/*
  #rm -r /home/pi/Brain/removed/*

  echo "Uploading pictures to Server"
  # exp upload.exp

  echo "\nDone\n"

fi
