#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

# Testing code, has nothing to do with main.py
def cam():
    KIPR.camera_load_config("andreas1")
    KIPR.camera_open()
    KIPR.camera_update()
def camFound(x):
    """Chanel x"""
    KIPR.camera_update()
    return KIPR.get_object_count(x)>0 and KIPR.get_object_area(x, 0)>200
def camPosX(x):
    """Chanel x, returns between -80 and 79"""
    KIPR.camera_update()
    return KIPR.get_object_center_x(0, 0)
    not(KIPR.get_object_count(0)>0 and KIPR.get_object_area(0, 0)>200 and 80<KIPR.get_object_center_x(0, 0)<100)

    while (not(KIPR.get_object_count(0)>0 and KIPR.get_object_area(0, 0)>200 and 80<KIPR.get_object_center_x(0, 0)<100)):
        KIPR.motor(0, 30)
        KIPR.motor(1, -30)
        
        KIPR.camera_update()
        count = KIPR.get_object_count(0)
        xPos = KIPR.get_object_center_x(0, 0)
        yPos = KIPR.get_object_center_y(0, 0)
        area = KIPR.get_object_area(0, 0)
        print("count: {}, xPos: {}, yPos: {}, area: {}".format(count, xPos, yPos, area))

    while (not(KIPR.get_object_count(0)>0 and KIPR.get_object_area(0, 0)>200 and 89<KIPR.get_object_center_x(0, 0)<91)):
        if (KIPR.get_object_center_x(0, 0)<90):
            KIPR.motor(0, 5)
            KIPR.motor(1, -5)
        else:
            KIPR.motor(0, -5)
            KIPR.motor(1, 5)
        
        KIPR.camera_update()
        count = KIPR.get_object_count(0)
        xPos = KIPR.get_object_center_x(0, 0)
        yPos = KIPR.get_object_center_y(0, 0)
        area = KIPR.get_object_area(0, 0)
        print("count: {}, xPos: {}, yPos: {}, area: {}".format(count, xPos, yPos, area))
           
	KIPR.ao() 
	print("object found")



#KIPR.wait_for_light()
print("After all")
def testAnalog():
    #print("left:" + str(KIPR.get_create_lcliff_amt()))
    print("left front:" + str(KIPR.get_create_lfcliff_amt()))
    #print("Right" + str(KIPR.get_create_rcliff_amt()))
    print("right front:" + str(KIPR.get_create_rfcliff_amt()))

def setup():
    print("Setup, connecting")
    KIPR.create_connect()
    # calibrations???
    KIPR.set_create_distance(0)
    KIPR.set_create_total_angle(0)
    # start shutdown timer ##disabled 4 testing
    ## wait4light()
    ## KIPR.shut_down_in(119)

setup()

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


#gripperHeight(1400)


while True:
    testAnalog()
    KIPR.msleep(1000)
    KIPR.enable_servos()

#servo 0: 0 - 1400
#Servo 1: 1000 - 2074
#servo 2: 1400 - 2047



#http://192.168.125.1:8888/#/apps/home