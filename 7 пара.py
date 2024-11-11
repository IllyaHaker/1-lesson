class Human:
    
    def __init__(self, name):
        self.__name = name
        
    def info(self):
        print("Name -", self.__name)
        
        
class Student(Human):

    def __init__(self, name, schoolName):
        self.__scName = schoolName
        super().__init__(name)

    def info(self):
        print("Student")
        super().info()
        print("School: ", self.__scName)


h = Human('Vasya')
h.info()

s = Student("Petya", "IT STEP")
s.info()