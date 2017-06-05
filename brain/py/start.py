
import glob
import colorful

print '\n-------------\n'

noshow = len(glob.glob('/home/pi/Brain/uploaded/ready/*'))
print colorful.bold_orange('NEW IMAGES:'), colorful.bold_orange(noshow)

print '\n-------------\n'
