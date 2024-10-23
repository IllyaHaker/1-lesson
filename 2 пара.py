class Student :
    print("Hi")


    def __init__(self, name="No name", height=160, age=15):
      self.name = name
      self.height = height
      self.age = age

    def addYear(self):
        if self.age < 100:
            self.age +=1

    def study(self):
        print("I studing")

    def info(self):
        print(f"Name   - {self.name}")
        print(f"Age    - {self.age}")
        print(f"Height - {self.height}")

    def __str__(self):
        return f"Name   - {self.name}\n" + f"Age    - {self.age}\n" + f"Height - {self.height}\n"

student1 = Student("Anton", 180)
student1.addYear()
print(student1)


#student2 = Student("Abobycov")
#print(student2.name)
