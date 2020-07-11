# Assignment 5
# Program 1

# Enter two numbers from user and store them in two variables.
# Define 4 functions which performs calculations of these two numbers and print the outout.
# - add()
# - subtract()
# - divide()
# - multiply()


number1 = input("Enter input for 1st number: ")
number1 = float(number1)

number2 = input("Enter input for 2nd number: ")
number2 = float(number2)


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def divide(number1, number2):
    return number1 / number2


def multiply(number1, number2):
    return number1 * number2


print(f"{number1} + {number2} = {add(number1, number2)}")
print(f"{number1} - {number2} = {subtract(number1, number2)}")
print(f"{number1} / {number2} = {divide(number1, number2)}")
print(f"{number1} * {number2} = {multiply(number1, number2)}")


# Program 2 - Define a function that takes a list e.g price_list = [10,20,30,40] and returns the total.

def sum(price_list):
    total = 0
    for i in range(0, len(price_list)):
        total += price_list[i]
    return total


count = input("Enter how many numbers you would like to add in this list: ")
count = int(count)

price_list = []
for i in range(0, count):
    temp = float(input(f"Enter price for product {i + 1}: "))
    price_list.append(temp)
print(f"Total bill amount = {sum(price_list)}")


# Program 3
# Define a function that takes a dict and print an item or fruites which has a value greater than 50.
# E.g  price_dict = {"mango": 60, "apple": 20, "banana": 10, "oranage": 50", "pineappale": 55}


def pricegreaterthan50(price_dict):
    for key, value in price_dict.items():
        if value > 50:
            print(str(key) + " : " + str(value))


count_items = int(input("Enter number of items in the dictionary: "))
products = {}
for i in range(0, count_items):
    item_name = input(f"Enter item name for product {i + 1}: ")
    price = float(input(f"Enter item price for product {i + 1}: "))
    products[item_name] = price

print(f"List of all products: {products}")
print("List of all products whose price > 50")
pricegreaterthan50(products)

