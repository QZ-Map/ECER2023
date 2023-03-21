class Wheels: 
    """ The Wheel class represents a pair of motors that are connected to a single physical wheelsystem
    It provides methods for controlling the movement of the wheels """
    def __init__(self, portRight, portLeft, diameter, spacing):    
        self.motorRight = Motor(portRight)
        self.motorLeft = Motor(portLeft)
        self.diameter = diameter
        self.spacing = spacing
        
        self.wheelU = 3.14159265359 * self.diameter   
        self.rotarionU = 3.14159265359 * self.spacing
        
    
    def distanceToTicks(self, distance):
        """ calculate the number of ticks required to travel a given distance """
        return int(distance / self.wheelU * 1800)
    def ticksToDistance(self, ticks):
        """ calculate the distance travelled given a number of ticks """
        return ticks / 1800 * self.wheelU
    def angleToTicks(self, angle):
        """ calculate the number of ticks required to rotate a given angle """
        return int(angle / 360 * 1800)
    def ticksToAngle(self, ticks):
        """ calculate the angle of rotation given a number of ticks """
        return ticks / 1800 * 360
    def distanceToAngle(self, distance):
        """ calculate the angle of rotation required to travel a given distance """
        return distance / self.wheelU * 360
    def angleToDistance(self, angle):
        """ calculate the distance travelled given a rotation angle """
        return angle / 360 * self.wheelU    
    
              

    def gmpc(self):
        """Get the average motor position counter value for the two motors."""
        return (self.motorRight.gmpc() + self.motorLeft.gmpc()) // 2

    def cmpc(self):
        """Clear the motor position counter for both motors."""
        self.motorRight.cmpc()
        self.motorLeft.cmpc()

    def freeze(self):
        """Stop both motors with active braking."""
        self.motorRight.freeze()
        self.motorLeft.freeze()

    def gmd(self):
        """Check if both motors have reached their goals."""
        return self.motorRight.gmd() and self.motorLeft.gmd()

    def bmd(self):
        """Wait until both motors have reached their goals."""
        self.motorRight.bmd()
        self.motorLeft.bmd()

    def fd(self, percentVelocity):
        """Sets the motor to move forward at the specified percentage of maximum velocity."""
        self.motorRight.fd(percentVelocity)
        self.motorLeft.fd(percentVelocity)

    def bk(self, percentVelocity):
        """Sets the motor to move backward at the specified percentage of maximum velocity."""
        self.motorRight.bk(percentVelocity)
        self.motorLeft.bk(percentVelocity)

    def mapv(self, percentVelocity):
        """Set the goal velocity for both motors in ticks per second."""
        self.motorRight.mapv(percentVelocity)
        self.motorLeft.mapv(percentVelocity)

    def mapp(self, percentPower):
        """Set the goal power level for both motors as a percentage of full power."""
        self.motorRight.mapp(percentPower)
        self.motorLeft.mapp(percentPower)

    def off(self):
        """Turn off both motors."""
        self.motorRight.off()
        self.motorLeft.off()

    def mav(self, speed):
        """ Move both motors with speed in ticks per second """
        self.motorRight.mav(speed)
        self.motorLeft.mav(speed)
        
    def mtp(self, speed, pos):
        """ Move both motors with speed in ticks per second to absolute position """
        self.motorRight.mtp(speed, pos)
        self.motorLeft.mtp(speed, pos)
        
    def mrp(self, speed, deltaPos):
        """ Move both motors with speed in ticks per second to relative position """
        self.motorRight.mrp(speed, deltaPos)
        self.motorLeft.mrp(speed, deltaPos)
        
    def standRotate(self, angle, speed):
        """ Rotate at current Position with both motors moving in opposite directions and clockwise beeing positive """
        rotationDistance = self.distanceToTicks(angle / 360 * self.rotarionU)
        self.motorRight.mrp(speed, rotationDistance/2)
        self.motorLeft.mrp(speed, rotationDistance/2)