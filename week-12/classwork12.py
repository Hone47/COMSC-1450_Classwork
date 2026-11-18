# q1

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")


my_cat = Cat("Whiskers")
my_cat.eat()
my_cat.meow()


# q2

class Shape:
    def describe(self):
        print("This is a generic shape.")


class Square(Shape):
    def describe(self):
        print("This is a square with 4 equal sides.")


s1 = Shape()
s1.describe()

s2 = Square()
s2.describe()


# q3

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class CubeBase(Rectangle):
    def perimeter(self):
        return 2 * (self.length + self.width)


box = CubeBase(5, 3)

print("Area:", box.area())
print("Perimeter:", box.perimeter())


# q4

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"


mgr = Manager("Sarah", 90000, "Engineering")
print(mgr.get_details())


# q5

class Vehicle:
    def __init__(self, brand, fuel_level):
        self.brand = brand
        self.fuel_level = fuel_level

    def drive(self, miles):
        self.fuel_level -= miles * 0.5
        print(f"{self.brand} drove {miles} miles.")


class ElectricCar(Vehicle):
    def __init__(self, brand, fuel_level, battery_health=100):
        super().__init__(brand, fuel_level)
        self.battery_health = battery_health

    def drive(self, miles):
        print("Silent electric drive...")
        super().drive(miles)
        self.battery_health -= 0.1


ev = ElectricCar("Tesla", 80)
ev.drive(20)

print(f"Fuel/Charge left: {ev.fuel_level}, Battery Health: {ev.battery_health}")


# q6 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_cost):
        super().__init__(name, price)
        self.warranty_cost = warranty_cost

    def final_price(self):
        return super().final_price() + self.warranty_cost


class ClearanceElectronic(ElectronicProduct):
    def __init__(self, name, price, warranty_cost, discount_percent):
        super().__init__(name, price, warranty_cost)
        self.discount_percent = discount_percent

    def final_price(self):
        total = super().final_price()
        return total - (total * self.discount_percent / 100)


laptop = ClearanceElectronic("Laptop", 1000, 100, 20)
print(laptop.final_price())