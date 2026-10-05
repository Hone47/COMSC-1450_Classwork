def countdown(n):
  if n <= 0:
    print("Liftoff!")
    return 
  print(n, end=", ")
  return countdown(n-1)

# countdown(5)

def print_range(start, end):
  if start > end:
    return
  print(start)
  return print_range(start+1, end)
  
  
# print_range(1,10)

def factorial(n):
  if n == 0:
    return 1
  
  return n * factorial(n-1)

# print(factorial(5))

def count_down_evens(n):
  if n < 0:
    print("done")
    return 
  print(n)
  return count_down_evens(n-2)

count_down_evens(10)

def power_of_two(n):
  if n == 0:
    return 1
  return 2 * power_of_two(n - 1)

print(power_of_two(5))

ex6 = lambda x,y : x if x > y  else  y 

print(ex6(1,2))

ex7 = lambda x,y : "Postive" if x > 0 else "Negative" 


ex8 = lambda x,y : x + y

import math 
ex9 = lambda radius : (math.pi *  math.pow(radius))
