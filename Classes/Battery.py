class Battery:
    """Static methods for getting battery information."""

    @staticmethod
    def power_level():
        """Returns the device's current battery capacity as a float in the range [0, 1]."""
        return KIPR.power_level()

    @staticmethod
    def power_level_life():
        """Returns the device's current battery capacity as a float in the range [0, 1] for a LiFePO4 battery."""
        return KIPR.power_level_life()

    @staticmethod
    def power_level_lipo():
        """Returns the device's current battery capacity as a float in the range [0, 1] for a LiPo battery."""
        return KIPR.power_level_lipo()

    @staticmethod
    def power_level_nimh():
        """Returns the device's current battery capacity as a float in the range [0, 1] for a NiMH battery."""
        return KIPR.power_level_nimh()