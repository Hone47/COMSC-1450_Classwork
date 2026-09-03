num = int(input("Enter a number"))
if(num >= 60):
  print("yes")
else:
  print("no")
print(("the rest of the code"))


num2 = int(input("Enter a number"))
if(num%2 >= 1):
  print("number is odd")
else:
  print("number is even")
  

age = int(input("Enter your age"))
if(age >=20):
  print("Adult")
else:
  print("teenager")

temp = int(input("Enter your tempurature"))
if(age >80):
  print("Hot")
else:
  print("Not Hot")

number1 = int(input("Enter your number"))
number2 = int(input("Enter your number"))
if(number1 >number2):
  print(number1,"is greater")
elif(number2> number1):
  print(number2,"is greater")
else:
  print("number are the same")  

grade = int(input("Score"))
if(grade > -1 and grade < 101 ):
  print("valid")
else:
  print("Not Valid")

number1 = int(input("Enter your number"))
number2 = int(input("Enter your number"))
if(number1 == number2):
  print("number are different")
else:
  print("number are the same") 



pin = int(input("Pin"))
if(pin == 1234):
  print("valid")
else:
  print("Not Valid")
  
temp = int(input("Enter your tempurature"))
if(temp < 100):
  print(temp,"is very hot")
elif(temp<100 and  temp>80):
  print(temp,"is hot")
elif(temp < 80 and temp >60):
  print(temp, "warm")
else:
  print(temp,"is cool")


grade = int(input("Enter your grade"))
if(grade <= 90):
  print(grade,"is A")
elif(grade<90 and  grade>=80):
  print(grade,"is B")
elif(grade<80 and grade>=70):
  print(grade, "is C")
elif(grade<70 and grade>69):
 print(grade, "is D")
else:
  print(grade,"is F")
  
  
  

number1 = int(input("Enter your number"))
number2 = int(input("Enter your number"))
number3 = int(input("Enter your number"))

if(number1 >number2 and number1 > number3):
  print(number1,"is greater")
elif(number2 > number1 and number2 > number3):
  print(number2,"is greater")
elif(number3 > number1 and number3 > number2):  
  print(number3,"is greater")
else:
  print("number are the same")


age = int(input("Enter your age"))
if(age < 13):
  print("price is 5 dollars")
elif(age <13 and age > 18):
  print("price is 8 dollars")
elif(age < 65  and age >= 18):
  print("Adult")
elif(age <=65):
 print("price is 7 dollars")

number1 = int(input("Enter your number"))
number2 = int(input("Enter your number"))
operator = (input("Enter your operator +,-,*,/"))

if(operator == "+"):
  print(number1+number2)
if(operator == "-"):
  print(number1-number2)
if(operator == "*"):
  print(number1/number2)
if(operator == "/"):
  print(number1/number2)

