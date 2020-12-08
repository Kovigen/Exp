class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriprion_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' +self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        """Выводит пробег авто"""
        print("Пробег этого авто" + str(self.odometer_reading) + " км")

my_car = Car('audi', 'a4', '2017')
print(my_car.descriprion_name())

my_car.odometer_reading


