class Car:
    total_cars = 0

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"


    def fuel_type(self):
        return "prtol or diesel"
    @staticmethod
    def general_description():
        return "This is a car."
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size
    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."
    def fuel_type(self):
        return "electricity"
        
#my_tesla = ElectricCar("Tesla", "Model S", 100)
#print(isinstance(my_tesla, Car))
#print(isinstance(my_tesla, ElectricCar))

#print(my_tesla.brand)
#print(my_tesla.fuel_type())


#my_car = Car("Land Rover", "Defender")
#my_car.model = "Defender 80"
#Car("Land Rover", "Defender 90")
#print(my_car.general_description())
#print(my_car.model)



"""my_car = Car("Toyota", "Corolla")
print(my_car.brand) 
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Honda", "Civic")
print(my_new_car.brand)"""


class Battery:
    def battery_info(self):
        return "This is a battery."

class Engine:
    def engine_info(self):
        return "This is an engine."

class ElectricCartwo(Car, Battery, Engine):
    pass

my_new_tesla = ElectricCartwo("Tesla", "Model 3")
print(my_new_tesla.full_name())
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())