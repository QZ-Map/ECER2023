class Servo:
    def __init__(self, port: int):
        self.port = port
                
    def __str__(self) -> str:
        return str(self.get_position())
    
    
    def enable(self) -> None:
        """
        Enable a specific servo.
        """
        KIPR.enable_servo(self.port)
        
    def disable(self) -> None:
        """
        Disable a specific servo.
        """
        KIPR.disable_servo(self.port)
    
    def set_enabled(self, enabled: int) -> None:
        """
        Enable or disable a specific servo.

        Parameters:
        - enabled: The new enable setting 0: disabled 1: enabled
        """
        KIPR.set_servo_enabled(self.port, enabled)
        
    def get_enabled(self) -> int:
        """
        Check if a servo is enabled.

        Returns:
        - The servo enable setting 0: disabled 1: enabled
        """
        return KIPR.get_servo_enabled(self.port)
    
    def get_position(self) -> int:
        """
        Get the most recent commanded servo position.

        Returns:
        - The servo's position as an 11 bit integer (which is an integer between 0 and 2047)
        """
        return KIPR.get_servo_position(self.port)
    
    def set_position(self, position: int) -> None:
        """
        Set a new servo goal position.

        Parameters:
        - position: The new servo position, between 0 and 2047

        Note:
        - Even though the servos have a theoretical range between 0 and 2047, the actual range is often less. Setting the servo to a position that it cannot physically reach will cause the servo to audibly strain and will consume battery very quickly.
        """
        KIPR.set_servo_position(self.port, position)
        
    def slow_movement(self, position: int, time: int) -> None:
        
        
    @staticmethod
    def enable_all() -> None:
        """
        Enable all four servo channels.
        """
        KIPR.enable_servos()
    
    @staticmethod
    def disable_all() -> None:
        """
        Disable all four servo channels.
        """
        KIPR.disable_servos()
