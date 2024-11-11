from dataclasses import field


class Human:
    height = 160


    def info(self):
        print(self.height)

class Student(Human):
    def __init__(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if 0 < age < 100:
            self.__age = age

    def study(self):
        print("I`m study")


class LitlStudent(Student):
    pass


class Worker(Human):
    pass

# h = Human()
# print(h.height)
# print(h.age)
# h.info()
#

s = Student(15)
print(s.height)
print(s.getAge())
s.setAge(2000000)
print(s.getAge())
# s.info()
# s.study()



#
# w = Worker()
# w.info()
#
# ls = LitlStudent()
# ls.info()




# class Class1:
#     field = "Hello"
#     _field = "Hello_"
#     __field = "Hello__"
#
#     def info(self):
#         print(self.field)
#         print(self._field)
#         print(self.__field)

# c = Class1()
# c.info()
# print(c.field)
# print(c._field)
# print(c.__field)


class Class1:
    def __init__(self):
        print("Class 1")

    def func1(self):
        print("Funk 1")

class Class2(Class1):
    def __init__(self):
        super().__init__()
        print("Class 2")

    def info(self):
        super().func1()

c = Class2()
c.info()