"""1. A university evaluates applicants using the following rules:
An applicant is accepted if:
● GPA is at least 3.0 and SAT score is at least 1100, or
● GPA is at least 3.5 and SAT score is at least 1000.
However, an applicant must have a GPA of at least 2.5 to be considered.
Write a Python program that asks for the student's GPA and SAT score and
prints:
● "Accepted"
● "Rejected"
● "Invalid GPA" if GPA is outside 0.0–4.0
● "Invalid SAT score" if the SAT score is negative
"""
gpa = float(input("Gpa?"))
sat_score = int(input("Sat score?"))

if(gpa < 4.0 and gpa > 0.0 and sat_score > 0):
  if(gpa > 3.0 and sat_score > 1100):
    print("Accepted")
  elif(gpa > 3.5 and sat_score > 1000):
    print("Accepted")
else:
  print("Rejected")    

"""
2. Write a program that calculates shipping costs based on the package
weight and whether the customer has a premium membership.
Rules:
● Weight ≤ 2 kg → $5
● Weight > 2 kg and ≤ 5 kg → $10
● Weight > 5 kg and ≤ 10 kg → $15
● Weight > 10 kg → $25
Premium members receive free shipping if the package weighs 5 kg or less.
The program should reject zero or negative weights.
"""
membership = input("Premium membership y/n?")
weight = int(input("Weight of package?"))
cost = 0
if(weight < 0): 
  if(weight <= 2 ):
    if(membership =="y"):
      cost = 0
    else:
      cost = 5   
  elif(weight > 2 and weight<= 5):
    if(membership == "y"):
      cost = 0
    else:
      cost = 5   
  elif(weight > 5 and weight<= 10):
      cost = 15     
  elif(weight < 10):
    cost = 25
else:
  print("Weight is not valid")

"""
3. A restaurant calculates delivery fees based on order amount and
distance.
● Order ≥ $50 → Free delivery
● Order $30–$49.99 and distance ≤ 5 km → $3
● Order below $30 and distance ≤ 5 km → $5
● Distance greater than 5 km → Additional $2
Write a program that asks for the order amount and delivery distance and
calculates the total delivery fee."""

distance = int(input("km of distance?"))
order_cost = float(input("cost of order?"))
delivery_fee = 0.0
if(order_cost > 0 and distance > 0):
  if(order_cost >= 50):
    delivery_fee = 0
    
  if(order_cost > 30 and delivery_fee < 50 and distance <= 5):
    delivery_fee = 5
  elif(order_cost > 30 and delivery_fee < 50 and distance > 5):
    delivery_fee = 7
else:
  print("Invalid input")