def calculate_ticket_sales():
  total_sales = 0
  tickets = 0
  while True:
    age = int(input("What is the age"))
    if(age == -1):
     break
    if(age < 5):
      
      tickets += 1
    elif(age <= 5 and age>=12):
      total_sales += 8
      tickets += 1
    elif(age <=13 and age >=59):
      total_sales += 12
      tickets += 1
    else: 
      total_sales += 9
      tickets += 1
      
  if(tickets >= 10):
    discount = total_sales * .05
    total_sales = total_sales - discount
    return total_sales, tickets
  
def main():
  total_sales, tickets = calculate_ticket_sales()
  print(total_sales,tickets)
  
main()