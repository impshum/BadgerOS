#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

cd ~/

if [ -z "$(ls -A sdcard/Pinky/uploaded/)" ]; then
  printf "${RED}No new pictures to process\n${NC}"
else
  printf "${GREEN}Found new pictures to process\n${NC}"

  echo "Moving pictures"

  find sdcard/Pinky/uploaded/ -mindepth 2 -type f -print -exec mv {} sdcard/Pinky/ready/ \;

  echo "Renaming pictures"

  cd sdcard/Pinky/ready/

  num=1
  for file in *.jpg; do
    mv "$file" "$(printf "%u" $num).jpg"
    let num=$num+1
  done

  echo "Uploading pictures to Brain"
  # exp upload.exp

  cd ~/

  echo "Removing pictures"
  rm -r sdcard/Pinky/uploaded/*
  # rm -rf sdcard/Pinky/ready/*

  echo "Done"
fi
