class Magnetometer:
    @staticmethod
    def magneto_x():
        """
        Gets the sensed x magneto value

        Returns:
            The latest signed x magneto value
        """
        return KIPR.magneto_x()

    @staticmethod
    def magneto_y():
        """
        Gets the sensed y magneto value

        Returns:
            The latest signed y magneto value
        """
        return KIPR.magneto_y()

    @staticmethod
    def magneto_z():
        """
        Gets the sensed z magneto value

        Returns:
            The latest signed z magneto value
        """
        return KIPR.magneto_z()

    @staticmethod
    def magneto_calibrate():
        """
        Initiates a calibration of the magnetometer

        Note:
            Not Yet Implemented

        Returns:
            1: success 0: failure
        """
        return KIPR.magneto_calibrate()