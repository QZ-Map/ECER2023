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
        return KIPR.get_motor_done(self.port)
    
    def bmd(self):
        """Waits until the motor has finished moving."""
        KIPR.block_motor_done(self.port)
    
    def fd(self, percentVelocity):
        """Sets the motor to move forward at the specified percentage of maximum velocity."""
        KIPR.fd(self.port, percentVelocity)
    
    def bk(self, percentVelocity):
        """Sets the motor to move backward at the specified percentage of maximum velocity."""
        KIPR.bk(self.port, percentVelocity)
    
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