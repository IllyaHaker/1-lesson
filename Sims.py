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
        if self.car == None:
            print("Пішов на роботу :(")
        else:
            if self.car.driwe(random.randint(1, 10) * 10):
                print("Поїхав працювати ")
            else:
                print("Пішов на роботу")


    def cleaning(self):

        choice_of_cleaning = random.randint(1, 2)
        if choice_of_cleaning == 1 and self.house.pollution >=10:
            print('Я сьогодні прибираю пил')
            self.house.pollution -= 5
        elif choice_of_cleaning == 2 and self.house.pollution >=0:
            self.house.pollution =0
            print('Я сьогодні роблю генеральне прибирання')
        else:
            self.chill()



    def eat(self):
        self.house.food -= random.randint(1, 10)
        self.house.pollution += random.randint(2, 8)
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
        self.house.pollution += random.randint(5, 15)
        print("Відпочив")

    def info(self):
        print(f"Грош - {self.money}")
        print(self.house)
        if self.car != None:
            print(self.car)

    def live(self, day):
        print(f"день {day}")
        choice = random.randint(1, 5)
        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        elif choice == 4:
            self.chill()
        elif choice == 5:
            self.cleaning()

        if self.money > 1000:
            print('Купляємо авто')
            self.money -= 500
            self.car = Car('Lexus RX 350')

        if self.house.pollution >= 90:
            print('Замовляю клінінг')
            self.money -= 100
            self.house.pollution = 0
        self.info()





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
            print('Подорож не можлива.Low fuel. Додай пального ')
            self.fuel += random.randint(0, 3)
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
        return f"Авто {self.model} - бензин {self.fuel} л, стан - {int(self.state)} %"


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
