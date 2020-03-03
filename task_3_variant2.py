class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
        self.odometer += distance
        return self.odometer

    def __subtract_fuel(self, liters):
        self.fuel -= liters

    def drive(self, distance):
        liters = distance // 10
        if liters <= self.fuel:
            self.__add_distance(distance)
            self.__subtract_fuel(liters)
            print('Let’s drive!')
        else:
            
            print('Need more fuel, please, fill more!')

    def __str(self):
        print(f'Car {self.model} {self.year} {self.fuel} {self.odometer}')


car1 = Car('Ford','Mondeo', 2009)
print(car1.model)
print(car1.year)
car1.drive(380)
print(car1.odometer)
print(car1.fuel)
