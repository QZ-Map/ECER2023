#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

#KIPR=ctypes.CDLL("./libkipr.so")

### Strat management ###
### stratname = id
normalRisk = 1
lowRisk = 0
HighRisk = 2
### Setstrat: strat = stratname
strat = normalRisk
### check strat: strat == stratname

####
def setup():
    print("Setup, connecting")
    KIPR.create_connect()
    # calibrations???
    KIPR.set_create_distance(0)
    KIPR.set_create_total_angle(0)
    # start shutdown timer ##disabled 4 testing
    ## wait4light()
    ## KIPR.shut_down_in(119)

def wait4light(): # non functional right now
    """ only continuies when starting light has been activated
    """
    print("waiting for light")
    port = 7 ## random port
    KIPR.wait_for_light(port)

### temporary for functions that belong into an other file
fwd = 100
bwd = -100

def driveStraight(speed_mm_s, distance_mm):
    """ speed in mm/sec, distance in mm
        not testet!!
        Backward unsafe!!! backward!!
    """
    distance_mm *= 1.1
    speed = speed_mm_s 
    distance = distance_mm
    #print("driving straight for" + distance + "mm")
    d0 = KIPR.get_create_distance()
    if speed > 0:
        while d0 + distance > KIPR.get_create_distance():
            angle = KIPR.get_create_total_angle()
            KIPR.create_drive_direct(speed, speed)
            if KIPR.get_create_total_angle() < angle:
                KIPR.create_drive_direct(speed, speed/2)
                print("left")
            if KIPR.get_create_total_angle() > angle:
                KIPR.create_drive_direct(speed/2, speed)
                print("right")
            KIPR.msleep(1) # should we delete this?
    else:
        print ("hit the else")
        while d0 - distance < KIPR.get_create_distance():
            KIPR.create_drive_direct(speed, speed)
            KIPR.msleep(1) # should we delete this?
    KIPR.create_drive_direct(0, 0)
    return

######################################
print("before setup")
setup()
print("after setup")
driveStraight(fwd, 1000) #need to check distance accuracy
driveStraight(-300, 500) #need to check distance accuracy
print("after all")

#http://192.168.125.1:8888/#/apps/home


