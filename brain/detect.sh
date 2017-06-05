#!/bin/sh

while true
do
    python /Users/impshum/Desktop/halo/brain/py/start.py
    find /Users/impshum/Desktop/halo/brain/ready/ -name "*.jpg" -exec python /Users/impshum/Desktop/halo/brain/py/detect.py {} \;
    python /Users/impshum/Desktop/halo/brain/py/results.py
    sleep 600
done
