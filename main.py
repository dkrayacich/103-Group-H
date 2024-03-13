from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    tooLeft = False
    tooRight = False
    while not tooLeft or tooRight:


        counter = 0
        for dist in rover.laser_distances[16:21]:
            if dist > 2:
                counter+= 1
            if counter >= 3:
                tooLeft = True
                break

        counter = 0
        for dist in rover.laser_distances[13:17]:
            if dist < 0.3:
                counter += 1
            if counter >= 2:
                tooRight = True
                break

