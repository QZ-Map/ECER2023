class Motor:    
    def __init__(self, port: int):
        self.port = port
                
    def __str__(self) -> str:
        return str(self.gmpc())
    
    
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
    
    @staticmethod
    def alloff() -> None:
        """Stops all motors on the robot and releases their current positions."""
        KIPR.alloff()