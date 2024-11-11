class Animal:
    def __init__(self, name):
        self.__name = name

    def info(self):
        print("Name:", self.__name)


class Mammals(Animal):
    def move(self):
        print("I`m move")


class Fish(Animal):
    pass


class Cat(Mammals):
    def __init__(self, name, mouse):
        self.__mouse = mouse
        super().__init__(name)

    def info(self):
        super().info()
        print("Mouse: ", self.__mouse)

    def cathMouse(self):
        print("I`m cath mouse")
        self.__mouse += 1

# class Dog(Mammals):
#     pass

class GoldenFish(Fish):
    pass


cat = Cat("Tom", 10)
cat.info()
cat.cathMouse()
cat.info()
cat.move()