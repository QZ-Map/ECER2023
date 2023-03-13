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
turn = 100

def driveStraight(speed_mm_s, distance_mm):
    """ speed in mm/sec, distance in mm
        | for backward driving speed negative, distance positive
        | should return isBumped in the future
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

def rotateAbsolute(deg):
    print("rotating absolute to " + str(deg))
    rotate(deg - RealRotation(), turn)

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
    KIPR.msleep(5000) ## better safe than sorry
    return

def rotateLeft(deg):
    speed = fwd
    print("rotating left for " + str(deg) + "deg")
    return rotate(deg, speed)

def rotateRight(deg):
    speed = fwd
    print("rotating right for " + str(deg) + "deg")
    return rotate(-deg, speed)

def followLine(): # Delay in drive straight is bad!!!
    while True:
        if KIPR.get_create_lfcliff_amt() < 2000:
            rotateLeft(1)
        elif KIPR.get_create_rfcliff_amt() < 2000:
            rotateRight(1)
        else:
            driveStraight(fwd, 1)

def gripperHeight(height):
    """servo 0: 0 - 1400
    """
    if 0<= height and height <= 1400:
        KIPR.set_servo_position(0, height)
    else:
        print("number out of bounds!  servo 0: 0 - 1400")

def gripperGrip(value):
    """Servo 1: 1000 - 2074
    """
    if 1000<= value and value <= 2074:
        KIPR.set_servo_position(1, value)
    else:
        print("number out of bounds!  servo 0: 1000 - 2074 ")


def gripperTilt(value):
    """Servo 2: 1400 - 2047
    """
    if 1400<= value and value <= 2047:
        KIPR.set_servo_position(2, value)
    else:
        print("number out of bounds!  servo 0: 1400 - 2047")




######################################
print("before setup")
setup()
print("after setup")

#rotateAbsolute(10)
#rotateAbsolute(100)
#rotateAbsolute(-30)
#rotateAbsolute(0)

rotateLeft(3600)
rotateRight(3600)

#gripperHeight(0)
#driveStraight(fwd,15)
#gripperGrip(1000)
#driveStraight(bwd,15)
#rotateLeft(180)
#gripperHeight(1300)
#gripperGrip(2074)

#driveStraight(-fwd, 3000) #need to check distance accuracy
#driveStraight(-300, 500) #need to check distance accuracy
#rotateLeft(3600)
#rotateRight(3600)
print("after all")



#http://192.168.125.1:8888/#/apps/home