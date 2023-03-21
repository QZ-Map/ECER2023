class Gyrometer:
    @staticmethod
    def gyro_x():
        """Gets the sensed x rotation.

        Returns:
            The latest signed x rotation value.
        """
        return KIPR.gyro_x()

    @staticmethod
    def gyro_y():
        """Gets the sensed y rotation.

        Returns:
            The latest signed y rotation value.
        """
        return KIPR.gyro_y()

    @staticmethod
    def gyro_z():
        """Gets the sensed z rotation.

        Returns:
            The latest signed z rotation value.
        """
        return KIPR.gyro_z()

    @staticmethod
    def gyro_calibrate():
        """Initiates a calibration of the gyrometer.

        Note:
            Not Yet Implemented.

        Returns:
            1 if successful, 0 if failure.
        """
        return KIPR.gyro_calibrate()
