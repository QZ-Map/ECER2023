#!/usr/bin/python
import os, sys
import ctypes
#KIPR=ctypes.CDLL("/usr/lib/libkipr.so") # path on Create bot
KIPR=ctypes.CDLL("./libkipr.so")

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
    ##################################################################### wait4light()
    ################# KIPR.shut_down_in(119) #I don't know, how long the robot can run

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
        not testet for backward!!
    """
    speed = speed_mm_s 
    distance = distance_mm
    print("driving straight for" + distance + "mm" )
    d0 = KIPR.get_create_distance()
    while d0 + distance < KIPR.get_create_distance():
        angle = KIPR.get_create_total_angle()
        KIPR.create_drive_direct(speed, speed)
        if KIPR.get_create_total_angle() < angle:
            KIPR.create_drive_direct(speed, speed/2)
        if KIPR.get_create_total_angle() > angle:
            KIPR.create_drive_direct(speed/2, speed)
        KIPR.msleep(1) # should we delete this?

######################################
setup()
driveStraight(fwd, 100) #need to check distance accuracy


#http://192.168.125.1:8888/#/apps/home