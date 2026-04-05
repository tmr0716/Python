# Create a base class Person (name,age)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello! my name is {self.name} and I am {self.age} years old.")
a = input(str)
b = input(int)
person = Person(a,b)
person.greet()

# Create subclass Student with marks and methods to display grades
x = print('Excellent Marks')
y = print('Good Marks')
z = print('Need more efforts')
class Student(Person):
    def __init__(self, marks):
        self.marks = marks
    def greet(self):
        print(f"I got {self.marks} in this exam.")
m = input(int)
mark = Student(m)
mark.greet()
