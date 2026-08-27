#question 2
# firstname = input("First Name:")
# lastname = input("Last Name:")
# print("Hello",lastname,",", firstname)
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

#question 7
# width = float(input("Width of triangle?"))
# length = float(input("Length of triangle?"))

# print("Area of triangle is :", round(width * length,2))

#question 8 
name = input("Enter your name:")
budget = float(input("Enter monthly budget ($):"))
daily_cost = float(input("Enter daily food cost ($):"))
monthly = daily_cost * 30
remaining = budget-monthly
print('---BUDGET SUMMARY---')
print(name,"|Food:$",monthly,"| Remaining:$", remaining)