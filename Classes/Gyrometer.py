class Gyrometer:
    @staticmethod
    def gyro_x() -> int:
        """Gets the sensed x rotation.

        Returns:
            The latest signed x rotation value.
        """
        return KIPR.gyro_x()

    @staticmethod
    def gyro_y() -> int:
        """Gets the sensed y rotation.

        Returns:
            The latest signed y rotation value.
        """
        return KIPR.gyro_y()

    @staticmethod
    def gyro_z() -> int:
        """Gets the sensed z rotation.

        Returns:
            The latest signed z rotation value.
        """
        return KIPR.gyro_z()

    @staticmethod
    def gyro_calibrate() -> int:
        """Initiates a calibration of the gyrometer.

        Note:
            Not Yet Implemented.

        Returns:
            1 if successful, 0 if failure.
        """
        return KIPR.gyro_calibrate()
