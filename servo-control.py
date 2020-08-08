
"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

count = 0
angle = 0
while (count < 9):
    if (angle > 149):
            angle = 0
    else:
            kit.servo[0].angle = angle + 1  
    time.sleep(1)
    pass
