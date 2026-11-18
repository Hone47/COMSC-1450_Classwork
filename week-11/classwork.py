#q1
def safe_divide():
  while True:
      try:
          A = float(input("Enter numerator: "))
          B = float(input("Enter denominator: "))

          result = A / B
      except ValueError:
          print("Please enter valid numbers.")
      except ZeroDivisionError:
          print("Cannot divide by zero. Try again.")
      else:
          print("Result:", result)
          break
safe_divide()

#q2
cart = ["Laptop", "Headphones", "Backpack", "Water Bottle"]

try:
    index = int(input("Enter the index of the item you want to view: "))
    print(cart[index])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("That index does not exist in the cart.")

except Exception:
    print("An unexpected error occurred.")cart = ["Laptop", "Headphones", "Backpack", "Water Bottle"]

try:
    index = int(input("Enter the index of the item you want to view: "))
    print(cart[index])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("That index does not exist in the cart.")

except Exception:
    print("An unexpected error occurred.")
    

#q3
file = None

try:
    file = open("grades.txt", "r")

    grades = file.readlines()

    total = 0

    for grade in grades:
        total += int(grade)

    average = total / len(grades)

    print("Average grade:", average)

except FileNotFoundError:
    print("Warning: grades.txt was not found.")

except ValueError:
    print("Warning: File contains invalid data.")

finally:
    if file is not None:
        file.close()

    print("File cleanup routine complete.")
    
#q4
account_balance = 500

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal must be greater than $0.")

    if amount > account_balance:
        raise ValueError("Insufficient funds available.")

except ValueError as e:
    print(e)

else:
    account_balance -= amount

    print("Withdrawal successful!")
    print("Remaining balance:", account_balance)

