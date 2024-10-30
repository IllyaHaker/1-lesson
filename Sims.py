class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def info(self):
        pass

    def live(self):
        pass

    def is_alive(self):
        if self.money < 0:
            return False
        else:
            return True

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60   #l
        self.state = 100 #%


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#car = Car("Lexus RX 350")
job = Job("Programmer", 1000)

human = Human('Antonw', job=job)
