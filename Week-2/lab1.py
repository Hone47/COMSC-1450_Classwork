#question 1
name = input("What is your name?")
print("Welcome to the course", name)
#question 2
firstname = input("First Name:")
lastname = input("Last Name:")
print("Hello",lastname,",", firstname)
#question 3
X = 32
Y = 'Sara'
Z = 3.5

print("Type of x",type(X),"Type of y",type(Y),"Type of z",type(Z))

#question 4

print("A\nB\nC\nD\nE\nF\n")

#question 5
path = 'C:\\Users\\rick\\Documents'
menu = ''''
---SYSTEM MENU---
  1.Open File
  2.Save File
  '''
sentence = 'The professor said, \'Make sure you escape matching quotes!\''
print(path)
print(menu)
print(sentence)

#question 6
item_1 = "Keyboard"
total_cost = 45.00
class_item = "Electronic"
item_Age = 2
print(item_1, total_cost, class_item)
print("item age is:", item_Age)
#question 7
width = float(input("Width of triangle?"))
length = float(input("Length of triangle?"))

#print("Area of triangle is :", round(width * length,2))

#question 8 
name = input("Enter your name:")
budget = float(input("Enter monthly budget ($):"))
daily_cost = float(input("Enter daily food cost ($):"))
monthly = daily_cost * 30
remaining = budget-monthly
print('---BUDGET SUMMARY---')
print(name,"|Food:$",monthly,"| Remaining:$", remaining)

#question 9 
radius = float(input("enter your radius"))
pi = 3.14159

Area = pi*radius*2


#question 10 

Celsius = float(input("How much Celsius?"))
fahrenheit = ((Celsius*(9.0/5.0))+ 35)
print(Celsius, "C is ", fahrenheit,"F.")

#question 11
n1 = float(input("Enter your first number"))
n2 = float(input("Enter your second number"))
n3 = float(input("Enter your third number"))

Average = (n1 + n2 + n3)/3

print("Average = ", Average)

#question 12
x = input("Give me your first value")
y = input("Give me your second value")
z = x
print("x = ",x)
print("y = ",y)
y = x 
z = y
print("x = ",x)
print("y = ",y)

#question 13
original_price = float(input("Original price?"))
discount_percentage = float(input("Discount Percentage"))
tax_percentage = float(input("Tax percentage"))
final_price = original_price * (1 - discount_percentage/100)

print("Your final price is", final_price)
