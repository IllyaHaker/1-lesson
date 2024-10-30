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

        def is_alive(self):
            if self.progress < 2:
                rnd = 1
            if self.gladness < 2:
                rnd = 2
            if self.progress > 98:
                rnd = 2
            if self.energy < 2:
                rnd = 3
            if self.money < 5:
                rnd = 4
            else:
                rnd = random.randint(1, 4)