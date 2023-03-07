#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
#KIPR=ctypes.CDLL("./libkipr.so")

#########################################
### Strat management ###
### stratname = id
normalRisk = 1
lowRisk = 0
HighRisk = 2
### Setstrat: strat = stratname
strat = normalRisk
### check strat: strat == stratname
#########################################

def RealDistance():
    return KIPR.get_create_distance()* 0.8933333333333333
def setRealDistance(dist):
    KIPR.set_create_distance(dist/0.8933333333333333)
def RealRotation():
    return KIPR.get_create_total_angle() * 0.875
def setRealRotation(deg):
    KIPR.set_create_total_angle(deg/0.875)




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

### ^^^^^ temporary for functions that belong into an other file
fwd = 100
bwd = -100
turn = 250

def driveStraight(speed_mm_s, distance_mm):
    """ speed in mm/sec, distance in mm
        | for backward driving speed negative, distance positive
    """
    speed = speed_mm_s 
    distance = distance_mm
    print("driving straight for " + str(distance) + "mm")
    d0 = RealDistance()
    if speed > 0:
        while d0 + distance > RealDistance():
            KIPR.create_drive_direct(speed, speed)
            KIPR.msleep(1) # should we delete this?
    else:
        while d0 - distance < RealDistance():
            KIPR.create_drive_direct(speed, speed)
            KIPR.msleep(1) # should we delete this?
    KIPR.create_drive_direct(0, 0)
    return

def rotate(deg, speed):
    d0 = RealRotation()

    if deg > 0:
        while d0 + deg > RealRotation():
            KIPR.create_drive_direct(-speed, speed)
            KIPR.msleep(1) # should we delete this?
    else:
        while d0 + deg < RealRotation():
            KIPR.create_drive_direct(speed, -speed)
            KIPR.msleep(1) # should we delete this?
    KIPR.create_drive_direct(0, 0)
    return

def rotateLeft(deg):
    speed = fwd
    print("rotating left for " + str(deg) + "deg")
    return rotate(deg, speed)

def rotateRight(deg):
    speed = fwd
    print("rotating right for " + str(deg) + "deg")
    return rotate(-deg, speed)


######################################
print("before setup")
setup()
print("after setup")
driveStraight(-fwd, 3000) #need to check distance accuracy
#driveStraight(-300, 500) #need to check distance accuracy
#rotateLeft(3600)
#rotateRight(3600)
print("after all")



#http://192.168.125.1:8888/#/apps/home