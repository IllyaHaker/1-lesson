class Human:
    height = 160

    def info(self):
        print(self.height)


class Student(Human):
    pass

h = Human()
print(h.height)
h.info()