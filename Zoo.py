import random

class Animal:
    def __init__(self, name):
        self.__name = name


    def info(self):
        print("Name:", self.__name)



class Mammals(Animal):
    def move(self):
        print("I`m move")


class Fish(Animal):
    def swim(self):
        print("I`m swim")
    def eat(self):
        print("I`m eat")



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


class Dog(Mammals):
    def __init__(self, name, burglares):
        self.__burglares = burglares
        super().__init__(name)

    def info(self):
        super().info()
        print("burglares: ", self.__burglares)

    def cathburglar(self):
        print("I`m caught a burglar")
        self.__burglares += 1

class GoldenFish(Fish):
    def __init__(self, name, wish):
        self.__wish = wish
        super().__init__(name)

    def info(self):
        super().info()
        print("Wish: ", self.__wish)

    def impltmentwish(self):
        print("I`m impltment wish")
        self.__wish += 1

class Carp(Fish):
    def __init__(self, name, weight, age, catchs):
        self.__age = age
        self.__weight = weight
        self.__catchs = catchs
        super().__init__(name)

    def info(self):
        super().info()
        print("weight: ", self.__weight)
        print("age: ", self.__age)
        print("catchs: ", self.__catchs)

    def live(self):
        print("I lived 1 year")
        self.__age += 1
        self.__weight += random.randint(1, 3)
    def catchs(self):
        print("I was caught")
        self.__catchs += 1



cat = Cat("Tom", 10)
cat.info()
cat.cathMouse()
cat.info()
cat.move()
print("-"*30)
GF = GoldenFish("Aleftina", 0)
GF.info()
GF.impltmentwish()
GF.info()
GF.swim()
GF.eat()
print("-"*30)
Dog = Dog("Sharik", 0)
Dog.info()
Dog.cathburglar()
Dog.info()
Dog.move()
print("-"*30)
Carp = Carp("Dobruna", 0.5, 1, 0)
Carp.info()
Carp.catchs()

Carp.swim()
Carp.live()
Carp.info()
