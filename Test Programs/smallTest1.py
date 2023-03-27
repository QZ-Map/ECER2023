class Motor:    
    def __init__(self, port):
        self.port = port
                
    def __str__(self):
        return str(self.gmpc())
    
    
    def gmpc(self):
        """Returns the current position of the motor in ticks."""
        return KIPR.get_motor_position_counter(self.port)
    
    def cmpc(self):
        """Clears the current position of the motor in ticks."""
        KIPR.clear_motor_position_counter(self.port)
    
    def freeze(self):
        """Stops the motor and holds its current position."""
        KIPR.freeze(self.port)
    
    def gmd(self):
        """Returns 1 if the motor has finished moving, 0 otherwise."""
        return bool(KIPR.get_motor_done(self.port))
    
    def bmd(self):
        """Waits until the motor has finished moving."""
        KIPR.block_motor_done(self.port)
    
    def fd(self):
        """Sets the motor to move forward at full velocity."""
        KIPR.fd(self.port)
    
    def bk(self):
        """Sets the motor to move backward at full velocity."""
        KIPR.bk(self.port)
    
    def off(self):
        """Stops the motor and releases its current position."""
        KIPR.off(self.port)
    
    def mapv(self, percentVelocity):
        """Sets the motor to move at the specified percentage of maximum velocity."""
        KIPR.motor(self.port, percentVelocity)
    
    def mapp(self, percentPower):
        """Sets the motor to move at the specified percentage of maximum power."""
        KIPR.motor_power(self.port, percentPower)
    
    def mav(self, speed):
        """Sets the motor to move at the specified speed in -1500 to 1500 ticks / second."""
        KIPR.move_at_velocity(self.port, speed)
    
    def mtp(self, speed, pos):
        """Sets the motor to move to the specified position at the specified speed."""
        KIPR.move_to_position(self.port, speed, pos)
    
    def mrp(self, speed, delta_pos):
        """Sets the motor to move to the specified relative position at the specified speed."""
        KIPR.move_relative_position(self.port, speed, delta_pos)
    
    @staticmethod
    def alloff():
        """Stops all motors on the robot and releases their current positions."""
        KIPR.alloff()

     
        
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

    def fd(self):
        """Sets the motor to move forward at full velocity."""
        self.motorRight.fd()
        self.motorLeft.fd()

    def bk(self):
        """Sets the motor to move backward at full velocity."""
        self.motorRight.bk()
        self.motorLeft.bk()

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
        rotationDistance = self.distanceToTicks((self.rotarionU * angle) / 360)
        self.motorRight.mrp(speed, -int(rotationDistance))
        self.motorLeft.mrp(speed, int(rotationDistance))
  
  
  
class Analog:
    """
    This class provides an interface for reading analog sensor values.
    """
    def __init__(self, port):
        self.port = port
                
    def __str__(self):
        return str(self.analog())
    

    def analog(self):
        """
        Gets the 12-bit analog value of the sensor connected to the specified port.

        Returns:
            The latest 12-bit value of the port (a value in the range 0 to 4095).
        """
        return KIPR.analog(self.port)

    def analog10(self):
        """
        Gets the 10-bit analog value of the sensor connected to the specified port.

        Returns:
            The latest 10-bit value of the port (a value in the range 0 to 1023).
        """
        return KIPR.analog10(self.port)

    def analog8(self):
        """
        Gets the 8-bit analog value of the sensor connected to the specified port.

        Returns:
            The latest 8-bit value of the port (a value in the range 0 to 255).
        """
        return KIPR.analog8(self.port)

    def analog_et(self):
        """
        Gets the 10-bit analog value of the ET sensor connected to the specified port.

        Returns:
            The latest 10-bit value of the port (a value in the range 0 to 1023).
        """
        return KIPR.analog_et(self.port)

    def set_pullup(self, pullup):
        """
        Sets the analog pullup status for the sensor connected to the specified port.

        Args:
            pullup: A value of 0 (inactive) or 1 (active).
        """
        KIPR.set_analog_pullup(self.port, pullup)

    def get_pullup(self):
        """
        Gets the analog pullup status for the sensor connected to the specified port.

        Returns:
            The status of the analog pullup on the specified port.
        """
        return KIPR.get_analog_pullup(self.port)
    
    
    @staticmethod
    def analog_(port):
        return KIPR.analog(port)
    
    @staticmethod
    def analog10_(port):
        return KIPR.analog10(port)
    
    @staticmethod
    def analog8_(port):
        return KIPR.analog8(port)
    
    @staticmethod
    def analog_et_(port):
        return KIPR.analog_et(port)
    
    @staticmethod
    def set_pullup_(port, pullup):
        KIPR.set_analog_pullup(port, pullup)
        
    @staticmethod
    def get_pullup_(port):
        return KIPR.get_analog_pullup(port)      



class Servo:
    def __init__(self, port):
        self.port = port
                
    def __str__(self):
        return str(self.get_position())
    
    
    def enable(self):
        """
        Enable a specific servo.
        """
        KIPR.enable_servo(self.port)
        
    def disable(self):
        """
        Disable a specific servo.
        """
        KIPR.disable_servo(self.port)
    
    def set_enabled(self, enabled):
        """
        Enable or disable a specific servo.

        Parameters:
        - enabled: The new enable setting 0: disabled 1: enabled
        """
        KIPR.set_servo_enabled(self.port, enabled)
        
    def get_enabled(self):
        """
        Check if a servo is enabled.

        Returns:
        - The servo enable setting 0: disabled 1: enabled
        """
        return KIPR.get_servo_enabled(self.port)
    
    def get_position(self):
        """
        Get the most recent commanded servo position.

        Returns:
        - The servo's position as an 11 bit integer (which is an integer between 0 and 2047)
        """
        return KIPR.get_servo_position(self.port)
    
    def set_position(self, position):
        """
        Set a new servo goal position.

        Parameters:
        - position: The new servo position, between 0 and 2047

        Note:
        - Even though the servos have a theoretical range between 0 and 2047, the actual range is often less. Setting the servo to a position that it cannot physically reach will cause the servo to audibly strain and will consume battery very quickly.
        """
        KIPR.set_servo_position(self.port, position)        
        
    def timed_movement(self, position, time = 1000):
        """ Move the servo to a specific position in a specified total time in ms """
        currentPos = self.get_position()
        startPos = currentPos
        stepSize = 0
        stepTime = 0
        while stepTime == 0:
            stepSize += (1 if (position>currentPos) else -1)
            stepTime = int(time / ((position-currentPos)/stepSize))
        substepCount = (position-currentPos) // stepSize
        #print(stepTime, stepSize, substepCount)
        for x in range(1, substepCount+1):
            #print("move to: ", (startPos+stepSize*x), ", wait: ", stepTime)
            self.set_position(startPos + stepSize*x)
            KIPR.msleep(stepTime)
        #print("move to: ", position)
        self.set_position(position)
    
        
    @staticmethod
    def enable_all():
        """
        Enable all four servo channels.
        """
        KIPR.enable_servos()
    
    @staticmethod
    def disable_all():
        """
        Disable all four servo channels.
        """
        KIPR.disable_servos()





wheels = Wheels(0, 1, 69, 165)
servoHeight = Servo(0)
servoHead = Servo(1)
servoHeight.enable_all()

KIPR.msleep(1000) 

servoHeight.set_position(1530)
servoHead.set_position(0)

wheels.mrp(1000, 1900)
while not wheels.gmd():
    KIPR.msleep(10)  
wheels.mrp(1000, 1000)

wheels.standRotate(115, 1000)
while not wheels.gmd():
    KIPR.msleep(10)  
    
wheels.mrp(1000, 4000)
while not wheels.gmd():
    KIPR.msleep(10) 
    
        
while Analog.analog_(0) < 2500:
    wheels.mrp(1000, 50)
    KIPR.msleep(10)  
    
wheels.mrp(500, 350)
while not wheels.gmd():
    KIPR.msleep(10) 


servoHead.timed_movement(700, 500)
servoHeight.timed_movement(1480, 100)

wheels.mrp(1000, -2000)
while not wheels.gmd():
    KIPR.msleep(10)  

servoHeight.timed_movement(300, 1000)   #lift cube

wheels.standRotate(160, 500)
while not wheels.gmd():
    KIPR.msleep(10) 
    
    
wheels.mrp(1000, 12000)
while not wheels.gmd():
    KIPR.msleep(10) 
    
while Analog.analog_(0) < 2000:
    wheels.mrp(1000, 50)
    KIPR.msleep(10) 
    
wheels.mrp(1000, -400)
while not wheels.gmd():
    KIPR.msleep(10) 
    
#place cube
servoHeight.timed_movement(1480, 1000)
servoHead.timed_movement(0, 500)
servoHeight.timed_movement(300, 500)

print("finished")
servoHead.set_position(0)