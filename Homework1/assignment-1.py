# Receipt Generator & Currency Conversion
# You will create a simple Python program for an international retail shop.

# Assignment Requirements
# Create one Python script file that follows the requirements below in the exact order.

# Part 1 — Information Ingestion
# Your program must ask the user for the following information:

# The customer's name using the prompt: What is your name?
# The number of items purchased using the prompt: Enter the number of items:
# The price per item in USD using the prompt: Enter the price per item in USD:


# Make sure you use input() and convert numerical inputs to the appropriate data type.
 

# Part 2 — Data Processing
# Your program must:

# Calculate the USD subtotal: quantity × unit cost
# Use the following exchange rate: 1 USD = 0.92 EUR
# Calculate the total cost in Euros.
# Use Python's built-in round() function to round the Euro total to exactly 2 decimal places.


# Part 3 — Receipt Output


# Your program should display the information in a format similar to the example below.



# What is your name? Alice
# Enter the number of items: 4
# Enter the price per item in USD: 12.50


# Customer Profile: Alice
# Customer Profile:   50.00
# EUR Total: €   46.00


# System Complete
exchange_rate = 0.92
name = input("What is your name?")
num_items = int(input("Enter the number of items:"))
usd_price = round(float(input("Enter the price per item in USD:")),2)

usd_totalprice = usd_price * num_items
euro_totalprice = round(usd_totalprice * exchange_rate,2)
#print(f"variable:.2f") is used to format so prices display 2 decimal places over.
print("Customer Profile:", name,"\nCustomer Profile:", f"{usd_totalprice:.2f}","\nEUR total: €", f"{euro_totalprice:.2f}")