print('----------------------------------- Classroom Day 11 -----------------------------------')
print('====================================== OOPs ======================================')
class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    def greet(self):
        print(f"Hello, my name is {self.name} and I scored {self.marks} marks!")
s1 = Student("Sahil", 87)
s1.greet()

print('====================================== Instance and Class Variables ======================================')
class Student:
    school_name = "CodeDecode DYPIU"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
s1 = Student("Sahil", 90)
print(s1.school_name)
print(Student.school_name)

print('====================================== Methods in OOPs ======================================')
class calculator:
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b
print(calculator.add(10, 20))

print('====================================== Encapsulation ======================================')
class Account:
    def __init__(self, name, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        print("Updated balance:", self.__balance)
a1 = Account("Sahil", 500)
a1.deposit(200)

print('====================================== Inheritance ======================================')
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
    def show(self):
        super().show()
        print("Marks:", self.marks)
s = Student("Sahil", 95)
s.show()

print('====================================== Polymorphism ======================================')
class Dog:
    def sound(self): print("Woof!")
class Cat:
    def sound(self): print("Meow!")
for animal in [Dog(), Cat()]:
    animal.sound()

print('====================================== Abstraction ======================================')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started 🚗")
c = Car()
c.start()

print('====================================== Magic Methods ======================================')
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x},{self.y})"
v1 = Vector(2, 4)
v2 = Vector(3, 5)
print(v1 + v2)

print('====================================== Compostion vs Inheritance ======================================')
class Engine:
    def start(self): print('Engine Started')
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("🚗 Car moving...")
c = Car()
c.drive()