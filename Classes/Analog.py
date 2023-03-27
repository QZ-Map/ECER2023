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