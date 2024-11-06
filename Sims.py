import random

class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        self.money +=40
        print('Я сьогодн працюю')

    def cleaning(self):
        self.money +=20
        print('Я сьогодн працюю')

    def eat(self):
        self.house.food -= random.randint(1, 10)

        print('Я поїв')

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food += random.randint(5, 10)
        if self.car == None:
            print("Пішов")
        else:
            if self.car.driwe(random.randint(1, 10)*10):
                print("Поїхав")
            else:
                print("Пішов")

    def chill(self):
        self.money -= random.randint(10 , 20)
        print("Відпочив")

    def info(self):
        print(f"Грош - {self.money}")
        print(self.house)
        if self.car != None:
            print(self.car)

    def live(self, day):
        print(f"день {day}")
        choice = random.randint(1, 4)
        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        elif choice == 4:
            self.chill()

        if self.money > 1000:
            print('Купляємо авто')
            self.money -= 500
            self.car = Car('Lexus RX 350')
        self.info()
        print()


    def is_alive(self):
        if self.money < 0:
            return False
        else:
            return True

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Інформація про будинок: Їжа - {self.food}, забрудненн - {self.pollution}"

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60   #l
        self.state = 100 #%

    def driwe(self, h):
        delta_fuel = h * 0.1
        if self.fuel - delta_fuel < 0:
            print('Подореж не можлива.Low fuel ')
            return False
        else:
            print(f"Ми проїхали {h} км, витратили {delta_fuel} л пального")
            self.fuel -= delta_fuel
            self.state -= h*0.01
            return True

    def add_fuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
        else:
            self.fuel = 60

    def __str__(self):
        return f"Авто {self.model} - бензин {self.fuel} л, стан - {self.state} %"


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Інформація про пров.: ЗП - {self.salary}, Назва - {self.name}"

#car = Car("Lexus RX 350")
job = Job("Programmer", 1000)

human = Human('Anton', job=job)
for day in range(366):
    if human.is_alive() == False:
        break
    human.live(day)
