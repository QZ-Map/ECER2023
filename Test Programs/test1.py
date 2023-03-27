#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():
    KIPR.shut_down_in(2)
    
    while True:
        print("test")
        KIPR.msleep(500)

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()