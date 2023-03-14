class Accelerometer:
    """
    A class to represent the Accelerometer sensor.
    """

    @staticmethod
    def accel_x() -> int:
        """
        Gets the sensed x acceleration +/- 2G range, 1024 per G.
        This should be approximately 0 when at rest and flat on a table.

        Returns:
        --------
        int: The latest signed x acceleration value.
        """
        return KIPR.accel_x()

    @staticmethod
    def accel_y() -> int:
        """
        Gets the sensed y acceleration +/- 2G range, 1024 per G.
        This should be approximately 0 when at rest and flat on a table.

        Returns:
        --------
        int: The latest signed y acceleration value.
        """
        return KIPR.accel_y()

    @staticmethod
    def accel_z() -> int:
        """
        Gets the sensed z acceleration +/- 2G range, 1024 per G.
        This should be approximately -1024 when at rest and flat on a table.

        Returns:
        --------
        int: The latest signed z acceleration value.
        """
        return KIPR.accel_z()

    @staticmethod
    def accel_calibrate() -> int:
        """
        Initiates a calibration of the accelerometer.

        Note:
        ------
        This function is not yet implemented in the KIPR library.

        Returns:
        --------
        int: 1 if success, 0 if failure.
        """
        return KIPR.accel_calibrate()
