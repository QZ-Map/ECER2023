class Digitals:
    """
    The Digitals class interacts with the digital ports on the Wallaby robot.
    """ 
    def __init__(self, port: int) -> None:
        self.port = port
                
    def __str__(self) -> str:
        return str(self.digital())
    
    
    def digital(self) -> int:
        """Returns the current value of the specified digital port (1 if closed, 0 if open)."""
        return KIPR.digital(self.port)
    
    def set_digital_value(self, value: int) -> None:
        """Sets the value of the specified digital port in output mode."""
        KIPR.set_digital_value(self.port, value)
    
    def get_digital_value(self) -> int:
        """Returns the current value of the specified digital port (1 if closed, 0 if open)."""
        return KIPR.get_digital_value(self.port)
    
    def set_digital_output(self, out: int) -> None:
        """Sets the mode of the specified digital port (1 for output, 0 for input)."""
        KIPR.set_digital_output(self.port, out)
    
    def get_digital_output(self) -> int:
        """Returns the current mode of the specified digital port (1 for output, 0 for input)."""
        return KIPR.get_digital_output(self.port)
    
    def get_digital_pullup(self) -> int:
        """Returns the current pullup state of the specified digital port (deprecated)."""
        return KIPR.get_digital_pullup(self.port)
    
    def set_digital_pullup(self, pullup: int) -> None:
        """Sets the pullup state of the specified digital port (deprecated)."""
        KIPR.set_digital_pullup(self.port, pullup)  
    
    
    @staticmethod
    def digital_(port: int) -> int:
        """Returns the current value of the specified digital port (1 if closed, 0 if open)."""
        return KIPR.digital(port)

    @staticmethod
    def set_digital_value_(port: int, value: int) -> None:
        """Sets the value of the specified digital port in output mode."""
        KIPR.set_digital_value(port, value)

    @staticmethod
    def get_digital_value_(port: int) -> int:
        """Returns the current value of the specified digital port (1 if closed, 0 if open)."""
        return KIPR.get_digital_value(port)

    @staticmethod
    def set_digital_output_(port: int, out: int) -> None:
        """Sets the mode of the specified digital port (1 for output, 0 for input)."""
        KIPR.set_digital_output(port, out)

    @staticmethod
    def get_digital_output_(port: int) -> int:
        """Returns the current mode of the specified digital port (1 for output, 0 for input)."""
        return KIPR.get_digital_output(port)

    @staticmethod
    def get_digital_pullup_(port: int) -> int:
        """Returns the current pullup state of the specified digital port (deprecated)."""
        return KIPR.get_digital_pullup(port)

    @staticmethod
    def set_digital_pullup_(port: int, pullup: int) -> None:
        """Sets the pullup state of the specified digital port (deprecated)."""
        KIPR.set_digital_pullup(port, pullup)
