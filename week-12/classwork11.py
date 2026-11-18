class Student:
  def __init__(self,n,a):
    self.name = n
    self.a = a

s1 = Student("Sara", 18) 

#q1
class Book:
  def __init__(self,n,a,p):
    self.title = n
    self.author = a
    self.price = p
  def get_details(self):
    print(f'Title: {self.title}, Author: {self.author}, Price: ${self.price}')
  def apply_discount(self):
    self.price -= self.price*.10
book1 = Book("b1", "john", 10)
book2 = Book("b2", "john", 10)

book2.apply_discount()
book2.get_details()

#q2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Length: {self.length}, Width: {self.width}"


rectangle = Rectangle(5, 10)

print(rectangle)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

#q3

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50

    def feed(self):
        self.hunger -= 15

    def get_status(self):
        print(f"{self.name} the {self.species} has a hunger level of {self.hunger}.")


pet1 = Pet("Max", "Dog")
pet2 = Pet("Tweety", "Bird")

pet1.feed()
pet1.feed()

pet1.get_status()
pet2.get_status()

#q4

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0

    def drive(self, miles):
        self.odometer += miles

    def get_status(self):
        return f"A {self.make} {self.model} with {self.odometer} miles."


car1 = Car("Toyota", "Corolla")

car1.drive(150)
car1.drive(85)

print(car1.get_status())

#q5

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        self.grades.append(score)

    def get_average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)


student1 = Student("Bob")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

print(student1.name, "Average:", student1.get_average())

#q6

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def get_total(self):
        return sum(self.items.values())


cart = ShoppingCart()

cart.add_item("Milk", 3.50)
cart.add_item("Bread", 2.00)
cart.add_item("Eggs", 4.25)

print("Total:", cart.get_total())

#q6

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def get_total(self):
        return sum(self.items.values())


cart = ShoppingCart()

cart.add_item("Milk", 3.50)
cart.add_item("Bread", 2.00)
cart.add_item("Eggs", 4.25)

print("Total:", cart.get_total())


#q7

class BankAccount:
    def __init__(self, account_holder):
        self.__account_holder = account_holder
        self.__balance = 0.0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
        else:
            print("Insufficient funds!")


account = BankAccount("Alice")

account.deposit(100)

account.withdraw(150)

account.withdraw(40)

print("Final balance:", account.get_balance())

print(account.__balance)