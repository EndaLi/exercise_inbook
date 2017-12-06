
class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        long_name = str(self.year) + ' '+self.make+' '+self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading =  mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car need a gas tank!")

class Battery():

    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a  " + str(self.battery_size)+"-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

            message = "This car can go apprpxomately " +str(range)+\
                      " miles on a full charge.\n"
            print(message)

    def upgrade_bettery(self):
        print("I'm change the battery!")
        while self.battery_size != 85:
            self.battery_size = 85
        
class ElectricCar(Car):
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()




my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_bettery()
my_tesla.battery.get_range()


