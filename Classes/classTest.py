#!/usr/bin/python
import os, sys, math
import ctypes
#KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
    
class Motor:    
    def __init__(self, port: int):
        self.port = port
    
    def gmpc(self) -> int:
        """Returns the current position of the motor in ticks."""
        return KIPR.get_motor_position_counter(self.port)
    
    def cmpc(self) -> None:
        """Clears the current position of the motor in ticks."""
        KIPR.clear_motor_position_counter(self.port)
    
    def freeze(self) -> None:
        """Stops the motor and holds its current position."""
        KIPR.freeze(self.port)
    
    def gmd(self) -> bool:
        """Returns True if the motor has finished moving, False otherwise."""
        return bool(KIPR.get_motor_done(self.port))
    
    def bmd(self) -> None:
        """Waits until the motor has finished moving."""
        KIPR.block_motor_done(self.port)
    
    def fd(self, percentVelocity: int) -> None:
        """Sets the motor to move forward at the specified percentage of maximum velocity."""
        KIPR.fd(self.port, percentVelocity)
    
    def bk(self, percentVelocity: int) -> None:
        """Sets the motor to move backward at the specified percentage of maximum velocity."""
        KIPR.bk(self.port, percentVelocity)
    
    def off(self) -> None:
        """Stops the motor and releases its current position."""
        KIPR.off(self.port)
    
    def alloff(self) -> None:
        """Stops all motors on the robot and releases their current positions."""
        KIPR.alloff()
    
    def mapv(self, percentVelocity: int) -> None:
        """Sets the motor to move at the specified percentage of maximum velocity."""
        KIPR.motor(self.port, percentVelocity)
    
    def mapp(self, percentPower: int) -> None:
        """Sets the motor to move at the specified percentage of maximum power."""
        KIPR.motor_power(self.port, percentPower)
    
    def mav(self, speed: int) -> None:
        """Sets the motor to move at the specified speed."""
        KIPR.move_at_velocity(self.port, speed)
    
    def mtp(self, speed: int, pos: int) -> None:
        """Sets the motor to move to the specified position at the specified speed."""
        KIPR.move_to_position(self.port, speed, pos)
    
    def mrp(self, speed: int, delta_pos: int) -> None:
        """Sets the motor to move to the specified relative position at the specified speed."""
        KIPR.move_relative_position(self.port, speed, delta_pos)
        
    
        
class Wheels: 
    """ The Wheel class represents a pair of motors that are connected to a single physical wheelsystem
    It provides methods for controlling the movement of the wheels """
    def __init__(self, portRight:int, portLeft:int, diameter:float, spacing:float):    
        self.motorRight = Motor(portRight)
        self.motorLeft = Motor(portLeft)
        self.diameter = diameter
        self.spacing = spacing
        
        self.wheelU = math.pi * self.diameter   
        self.rotarionU = math.pi * self.spacing
        
    
    def distanceToTicks(self, distance: float) -> int:
        # calculate the number of ticks required to travel a given distance
        return int(distance / self.wheelU * 1800)
    def ticksToDistance(self, ticks: int) -> float:
        # calculate the distance travelled given a number of ticks
        return ticks / 1800 * self.wheelU
    def angleToTicks(self, angle: float) -> int:
        # calculate the number of ticks required to rotate a given angle
        return int(angle / 360 * 1800)
    def ticksToAngle(self, ticks: int) -> float:
        # calculate the angle of rotation given a number of ticks
        return ticks / 1800 * 360
    def distanceToAngle(self, distance: float) -> float:
        # calculate the angle of rotation required to travel a given distance
        return distance / self.wheelU * 360
    def angleToDistance(self, angle: float) -> float:
        # calculate the distance travelled given a rotation angle
        return angle / 360 * self.wheelU    
    
              

    def gmpc(self) -> int:
        """Get the average motor position counter value for the two motors."""
        return (self.motorRight.gmpc() + self.motorLeft.gmpc()) // 2

    def cmpc(self) -> None:
        """Clear the motor position counter for both motors."""
        self.motorRight.cmpc()
        self.motorLeft.cmpc()

    def freeze(self) -> None:
        """Stop both motors with active braking."""
        self.motorRight.freeze()
        self.motorLeft.freeze()

    def gmd(self) -> bool:
        """Check if both motors have reached their goals."""
        return self.motorRight.gmd() and self.motorLeft.gmd()

    def bmd(self) -> None:
        """Wait until both motors have reached their goals."""
        self.motorRight.bmd()
        self.motorLeft.bmd()

    def fd(self) -> None:
        """Move both motors forward at full power."""
        self.motorRight.fd()
        self.motorLeft.fd()

    def bk(self) -> None:
        """Move both motors backward at full power."""
        self.motorRight.bk()
        self.motorLeft.bk()

    def mapv(self, percentVelocity: int) -> None:
        """Set the goal velocity for both motors in ticks per second."""
        self.motorRight.mapv(percentVelocity)
        self.motorLeft.mapv(percentVelocity)

    def mapp(self, percentPower: int) -> None:
        """Set the goal power level for both motors as a percentage of full power."""
        self.motorRight.mapp(percentPower)
        self.motorLeft.mapp(percentPower)

    def off(self) -> None:
        """Turn off both motors."""
        self.motorRight.off()
        self.motorLeft.off()

    def alloff(self) -> None:
        KIPR.alloff()

    def mav(self, speed: int) -> None:
        """ Move both motors with speed in ticks per second """
        self.motorRight.mav(speed)
        self.motorLeft.mav(speed)
        
    def mtp(self, speed: int, pos: int) -> None:
        """ Move both motors with speed in ticks per second to absolute position """
        self.motorRight.mtp(speed, pos)
        self.motorLeft.mtp(speed, pos)
        
    def mrp(self, speed: int, deltaPos: int) -> None:
        """ Move both motors with speed in ticks per second to relative position """
        self.motorRight.mrp(speed, deltaPos)
        self.motorLeft.mrp(speed, deltaPos)
        
    def standRotate(self, angle: int, speed: int) -> None:
        """ Rotate at current Position with both motors moving in opposite directions and clockwise beeing positive """
        rotationDistance = self.distanceToTicks(angle / 360 * self.rotarionU)
        self.motorRight.mrp(speed, -rotationDistance/2)
        self.motorLeft.mrp(speed, rotationDistance/2)

def main():
    wheel = Wheels(0, 1, 10, 10)
    print(wheel.distToDegree(20*math.pi))
    
if __name__== "__main__":
    #sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
