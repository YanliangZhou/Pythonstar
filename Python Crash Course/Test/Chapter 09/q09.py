# 9-9 电瓶升级 ：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。这个方法检查电瓶容量，
# 如果它不是85，就将它设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，并再次调用
# get_range() 。你会看到这辆汽车的续航里程增加了。
from q09_1 import Car


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


    def upgrade_battery(self):
        """check and set battery"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


ford = ElectricCar("Ford", "Escape", 2014)
ford.battery.get_range()
ford.battery.upgrade_battery()
ford.battery.get_range()