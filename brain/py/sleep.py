import sys
import time

for remaining in range(1, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rComplete!\n")
