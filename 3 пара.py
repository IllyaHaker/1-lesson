import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 10
        self.alive = True
        self.energy = 60
        self.money = 25


    def study(self):
        print("я пішов навчатися")
        self.progress +=1
        self.energy -=1
        self.gladness -= 1

    def sleep(self):
        print('Я пішов спати')

        self.energy += 3
        self.gladness += 1

    def chill(self):
        print('Я пішов гуляти')
        self.money -= 5
        self.progress -= 1
        self.energy -= 1
        self.gladness += 2

    def work(self):
        print('Я - працювати')
        self.money +=10
        self.energy -= 1
        self.gladness -= 1



    def info(self):
        print(f'На сьгодні {self.name} має:')
        print(f'Задоволення : {self.gladness}')
        print(f'Знання      : {self.progress}')
        print(f'Енергія     : {self.energy}')
        print(f'Гроші     : {self.money}')

    def is_alive(self):
        if self.progress < 0:
            print(f'В мене в голові сміття, життя не має сенсу')
            self.alive = False
        if self.gladness < 0:
            print(f'В мене депрехін')
            self.alive = False
        if self.progress > 100:
            print(f'Я такий розумний, що вийшов з під контролю')
            self.alive = False
        if self.energy < 0:
            print(f'Low batari')
            self.alive = False
        if self.money < 0:
            print(f'Я збіднів')
            self.alive = False






    def live(self, day):
        print(f'День N{day} з життя {self.name}')
        print("-"*30)
        if self.progress < 4:
            rnd = 1
        if self.gladness < 4:
            rnd = 2
        if self.progress > 96:
            rnd = 2
        if self.energy < 4:
            rnd = 3
        if self.money < 5:
            rnd = 4
        else:
            rnd = random.randint(1, 4)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.chill()
        elif rnd == 3:
            self.sleep()
        elif rnd == 4:
            self.work()
        self.info()
        self.is_alive()
        print()





st = Student('Вася')

for d in range(1, 366):
    if st.alive == False:
        break
    st.live(d)