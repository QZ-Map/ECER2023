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
            #print(f"move to: {startPos+stepSize*x}, wait: {stepTime}")
            self.set_position(startPos + stepSize*x)
            KIPR.msleep(stepTime)
        #print(f"move to: {position}")
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
