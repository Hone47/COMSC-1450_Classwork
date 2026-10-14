import math

def evaluate_advanced_piecewise(x):
  if(x > 0):
    y = math.sqrt(math.log10(x) + math.exp(x)) * math.cos(math.radians(x))
    return y
  elif(x == 0):
    y = 0.0
    return y
  elif(x < 0):
    y = math.log10(math.fabs(x)) + math.pow(math.fabs(x), 3)
    return y
  
def main():
  num = float(input("Input a float to calculate"))
  result = evaluate_advanced_piecewise(num)
  print("Result from calculations", result)  


main()