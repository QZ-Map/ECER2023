#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

# Testing code, has nothing to do with main.py
def testAnalog():
    print("agr")
    print("left:" + str(KIPR.get_create_lcliff_amt()))
    print("left front:" + str(KIPR.get_create_lfcliff_amt()))
    print("Right" + str(KIPR.get_create_rcliff_amt()))
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
while True:
    print("gogog")
    testAnalog()
    KIPR.msleep(100)