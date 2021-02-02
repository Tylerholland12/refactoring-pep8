# by Kami Bigdely
# Docstrings and blank lines
"""Create sensor class."""
class OnBoardTemperatureSensor:
    """Initialialize the sensor class."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        pass
    def read_voltage(self):
        """return the voltage."""
        return 2.7
    def get_temperature(self):
        """return the temp."""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

"""Create CO sensor class."""
class CarbonMonoxideSensor:
    """Initialialize the CO class."""
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
    def get_carbon_monoxide_level(self):
        """return CO levels."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    def read_sensor_voltage(self):
        """return voltage."""
        # In real life, it should read from hardware.
        return 2.3
    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """return the change from voltage to CO level."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature

"""Create class to display temp."""
class DisplayUnit:
    """Initialialize the display unit class."""
    def __init__(self):
        self.string = ''
    def display(self,msg):
        """return the message."""
        print(msg)
"""Create class for CO device."""
class CarbonMonoxideDevice():
    """Initialialize the CO device class."""
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor
        self.display_unit = display_unit
    def display(self):
        """Initialialize the display class."""
        msg = 'Carbon Monoxide Level is : ' + str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor_two = OnBoardTemperatureSensor()
    co_sensor_two = CarbonMonoxideSensor(temp_sensor_two)
    display_unit_two = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor_two, display_unit_two)
    co_device.display()