
from random import randint

print("Вгадай число від 1 до 10")
PC = randint(0, 10)
user = 0
t = 0

while PC != user:
    if t == 3:
        print("Спроби закінчились")
        exit()
    user = int(input("твоє число:"))
    t += 1
    if PC > user:
        print("Більше")
    elif PC < user:
        print("Менше")

print("Перемога")





