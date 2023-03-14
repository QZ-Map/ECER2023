class Compass:
    """
    A class for interfacing with the KIPR Compass Sensor.
    """

    @staticmethod
    def calibrate() -> None:
        """
        Begin calibrating the compass.
        Will display the calibration parameter results which can be used in the future with set_compass_params
        Provided by Dr. Andrew H. Fagg and Twister Robotics
        """
        KIPR.calibrate_compass()

    @staticmethod
    def set_params(meanX: float, meanY: float, meanZ: float, W1: float, W2: float, div_E1: float, div_E2: float) -> None:
        """
        Set the compass parameters based on a previous calibration.
        Provided by Dr. Andrew H. Fagg and Twister Robotics

        :param meanX: a value provided by calibrate_compass
        :param meanY: a value provided by calibrate_compass
        :param meanZ: a value provided by calibrate_compass
        :param W1: a value provided by calibrate_compass
        :param W2: a value provided by calibrate_compass
        :param div_E1: a value provided by calibrate_compass
        :param div_E2: a value provided by calibrate_compass
        """
        KIPR.set_compass_params(meanX, meanY, meanZ, W1, W2, div_E1, div_E2)

    @staticmethod
    def get_angle() -> float:
        """
        Get the current compass heading.
        Provided by Dr. Andrew H. Fagg and Twister Robotics

        :return: the compass angle in radians
        """
        return KIPR.get_compass_angle()
