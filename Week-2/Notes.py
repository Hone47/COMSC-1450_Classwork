#types in python 
#int, float, str. bool 
#to see the type of you variable use func type()
#stings concating with '+' 


#type conversion in python 
#int() , float(), str(), 
print("Hello to the python class")
print(type(45))
print(type(45.98))
print(type("OKAY"))

print(5+6)

print("Hello"+"python")

print("hello" + str(2026))

x = 3
y = int(float(x))

#doesnt round only keeps the first decimal point.
print(type(x))
print(y) 

x = 5
y = 5
z = 5

x=y=z=5
print(x)
print(y)
print(z)

a = 1 
b = 2 
c = 3

a , b , c = 1, 2, 3


print("Welcome to the python class")
print("Fall")
print("2026")

print("Welcom to the python\nFall\n2026")


print('Hello to  "UST"')

#shorthand to concatotion
print("Hello to the python class" , 2026, "UST", 1500)
print(1,2,3,4, sep="%")

print("Welcome", end=" ")
print("2026")

x = '''Hello,
this is how you store a
paragraph 
in python'''

# Name = input("please enter your name ")
# print("Your name is", Name, "welcome to python")

num_1 = int(input("first number?"))
num_2 = int(input("second number?"))

print("your first num is", num_1, "and your second num is", num_2)

total = num_2 + num_1

print("Your total is", total)