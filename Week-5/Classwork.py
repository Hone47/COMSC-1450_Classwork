# import math 
# import random as r


#Q1
# distance = math.sqrt((math.pow(7-3,2) + math.pow(8-5,2)))
# print(distance)


#Q2
# degree = int(input("give me your degree"))

# radians = math.radians(degree)

# print("Your sin is", math.sin(radians), ". Your cosine is", math.cos(radians))

#Q3

# randomnum = r.random() 
# ranumletter = r.choice("ABCDEF")
# randomnumberten = r.randrange(10,50,10)

#Q4
def show_welcome_banner():
  print('''********************************
 Welcome to Python Programming!
********************************
        ''')

show_welcome_banner()
show_welcome_banner()
show_welcome_banner()

#Q5
def greet_user(username):
  print("Hello", username, ", welcome back!")

# name = input("what is your name?")
# greet_user(name)

#Q6
def checkNumEvenOrOdd(num):
  if(num%2 == 0):
    print("number is even")
  else:
    print("number is odd")
    
checkNumEvenOrOdd(5)

#Q7
def dollars_to_euro(amount):  
 # amount is in usd
 return amount * .92

money = dollars_to_euro(50)
print(money)

#Q8
def calculate_shipping(package_weight, distance_miles):
  total_shipping_weight = (package_weight * .5) + (.10 * distance_miles)
  return total_shipping_weight

print(calculate_shipping(12, 250),"$")

#Q9
def vowels(word):
  counter = 0
  for c in word:
    if c in "aeiou":
      counter +=1
  return counter

print(vowels("hello"))

#Q10
# Define a function named get_rectangle_stats that takes two parameters: length
# and width. Inside the body, calculate and return the area (length × width) of the
# rectangle.
