"""
3)Car
Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
самом начале проверьте, хватит ли вам бензина из расчета того, что машина
расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
то пусть этот метод добавляет эти километры к значению одометра, но не
напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью
приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
more!”
"""

class Car():
    """Класс принимает автомобиль """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer = 0
        self.__fuel = 70

    def __str__(self):
        return f"Марка: {self.make}\nМодель: {self.model}\nГод выпуска: {self.year}\nПоказания на одометре: {self.__odometer} "
    
    def drive(self, distance):
        distance_on_bak = 10*self.__fuel
        if distance <= distance_on_bak:
            print("“Let’s drive!”")
            print(f"Едим на расстояние {distance}км. бензина в баке {self.__fuel}л.")
            self.__fuel -= distance//10
            self.__odometer += distance    
            return self.__odometer
        else:
            print(f"Остаток бензина в баке {self.__fuel}л., этого не хватит чтобы проехать {distance}км.")

    def add_distance(self):
         return self.__odometer 

    def subtract_fuel(self):
        return self.__fuel
    
    def refeel_fuel(self):
        litr = int(input("Сколько литров хотите заправить?:"))
        self.__fuel += litr


car_1 = Car('Audi', 'RS6', 2019)
print(car_1)
car_1.drive(250)
car_1.drive(250)
car_1.drive(250)
car_1.refeel_fuel()
car_1.drive(250)
car_1.drive(450)
car_1.drive(350)
print(car_1)
