# Класс
class Doc:
    """Простая модель собаки"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Собака создана")

    def sit(self):
            """собака будет садиться по команле"""
            print(self.name.title() + " села")

    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " прыжок")
my_dog = Doc('Tomic', 4)

my_dog2 = Doc('Kovige', 7)

print(my_dog.name)
print(my_dog.age)
print(my_dog2.name)
print(my_dog2.age)

my_dog.jump()
my_dog2.sit()



