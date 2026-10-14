def calculate_payroll():
  total_payroll = 0.0
  while True:
    employee_wage = float(input("wage of employee?"))
    if(employee_wage < 0):
      break
    else:
      hours = int(input("how many hours?"))
      if(hours > 40):
        overtime = hours - 40
        salary = (40 * employee_wage) + (overtime * 1.5 * employee_wage)
      else:
        salary = hours * employee_wage
        
    total_payroll += salary
    
  if(total_payroll > 5000):
    print("The payroll exceeded the budget")
  
  return total_payroll

def main():
  total_payroll = calculate_payroll()
  print("The total payroll is",total_payroll, "$")
  
main()