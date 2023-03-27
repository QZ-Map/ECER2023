#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():
    ### ^^^^^ temporary for functions that belong into an other file
    # Driving vars
    fwd = 100
    bwd = -100
    turn = 100
    # Black line
    black = 2500
    
    
    def RealDistance():
        return KIPR.get_create_distance()* 0.8933333333333333
    def setRealDistance(dist):
        KIPR.set_create_distance(dist/0.8933333333333333)
    def RealRotation():
        return KIPR.get_create_total_angle() * 0.875
    def setRealRotation(deg):
        KIPR.set_create_total_angle(deg/0.875)
  
 
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

    def driveUntil(speed_mm_s, until):
        """ speed in mm/sec, Until in Lamda
            | for backward driving speed negative, distance positive
            | should return isBumped in the future
        """
        while not until():
            KIPR.create_drive_direct(speed_mm_s, speed_mm_s)
        KIPR.create_drive_direct(0, 0)
        return

    
    KIPR.camera_load_config("logs")
    KIPR.camera_open()
        
    while (not(KIPR.get_object_count(0)>0 and KIPR.get_object_area(0, 0)>400 and 89<KIPR.get_object_center_x(0, 0)<91)):
        if(KIPR.get_object_center_x(0, 0)<90):
            print("rotate(1, 100)")
        else:
            print("rotate(-1, 100)")

        KIPR.camera_update()
        count = KIPR.get_object_count(0)
        xPos = KIPR.get_object_center_x(0, 0)
        yPos = KIPR.get_object_center_y(0, 0)
        area = KIPR.get_object_area(0, 0)
        #print("count: {}, xPos: {}, yPos: {}, area: {}".format(count, xPos, yPos, area))
  
    driveUntil(100, lambda: (KIPR.get_object_count(0)>0 and KIPR.get_object_area(0, 0)>800 and 85<KIPR.get_object_center_x(0, 0)<95))
    
    while (not(KIPR.get_object_count(0)>0 and KIPR.get_object_area(0, 0)>400 and 89<KIPR.get_object_center_x(0, 0)<91)):
        if(KIPR.get_object_center_x(0, 0)<90):
            print("rotate(1, 100)")
        else:
            print("rotate(-1, 100)")

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()
 
 
 
 
 
 
 