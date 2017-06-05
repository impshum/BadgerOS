import glob
import colorful
import time
from time import gmtime, strftime
import sys

total1 = len(glob.glob('/home/pi/Brian/gallery/*'))
print colorful.bold_orange('NEW TOTAL:'), colorful.bold_orange(total1)

total2 = len(glob.glob('/home/pi/Brian/removed/*'))
print colorful.bold_red('AWW TOTAL:'), colorful.bold_red(total2)

time1 = strftime("%d-%m-%y", gmtime())
time2 = strftime("%H:%M:%S", gmtime())
print colorful.bold_yellow(time1), colorful.bold_yellow(time2)
