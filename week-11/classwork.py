class Student:
  def __init__(self,n,a):
    self.name = n
    self.a = a

s1 = Student("Sara", 18) 


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