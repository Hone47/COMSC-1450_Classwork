inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

inventory["bananas"] = 45

inventory["mangoes"] = 15

del inventory["oranges"]

print(inventory)

#q2
def get_stock(inventory, item):
    return inventory.get(item, "Not in stock")


inventory = {"apples": 50, "bananas": 45, "mangoes": 15}

print(get_stock(inventory, "apples"))
print(get_stock(inventory, "oranges"))

#q3
keys = ["Name", "Age", "Role"]
values = ["Alex", 24, "Developer"]

result = dict(zip(keys, values))

print(result)


#q4

scores = {
    "Alex": 85,
    "John": 40,
    "Sarah": 90,
    "Mike": 35
}

for key, value in scores.items():
    if value > 50:
        print(key, value)
        
#q5
original = {"A": 1, "B": 2, "C": 3}

inverted = {}

for key, value in original.items():
    inverted[value] = key

print(inverted)

#q6

default_settings = {
    "theme": "light",
    "fontsize": 12,
    "show_tips": True
}

user_settings = {
    "theme": "dark",
    "fontsize": 14
}

final_settings = default_settings.copy()
final_settings.update(user_settings)

print(final_settings)

#q7

fruits = {"apple", "banana", "orange"}

fruits.add("mango")

fruits.update(["grape", "watermelon"])

print(fruits)

#q8

fruits = {"apple", "banana", "orange"}

fruits.discard("banana")

print(fruits)

#q9
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

result = set1.intersection(set2)

print(result)