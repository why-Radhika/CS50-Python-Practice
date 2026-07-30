# ==========================================
# Set 1: Functions, Variables, Strings,
# Integers & Floats
# ==========================================

# -------------------------
# Question 1
# Greeting Program
# -------------------------

name = input("What is your name? ")
print("Hello,", name)


# -------------------------
# Question 2
# Favorite Language
# -------------------------

language = input("What is your favourite programming language? ")
print(language, "sounds interesting!")


# -------------------------
# Question 3
# Age Next Year
# -------------------------

age = int(input("Age: "))
print("Next year you will be", age + 1)


# -------------------------
# Question 4
# Simple Calculator
# -------------------------

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)


# -------------------------
# Question 5
# Full Name Formatter
# -------------------------

first_name = input("First name: ")
last_name = input("Last name: ")

print(f"Hello, {first_name} {last_name}")


# -------------------------
# Question 6
# Bill Splitter
# -------------------------

total_bill = 1250
friends = int(input("Number of friends: "))

print("Each person pays:", total_bill / friends)


# -------------------------
# Question 7
# Temperature Converter
# -------------------------

celsius = float(input("Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)


# -------------------------
# Question 8
# Custom Function
# -------------------------

def greet(name):
    print("Hello,", name)

greet("Radhika")


# -------------------------
# Question 9
# Return Value
# -------------------------

def square(n):
    return n * n

print(square(5))


# -------------------------
# Question 10
# Mini Profile Generator
# -------------------------

name = input("Name: ")
age = input("Age: ")
city = input("City: ")

print("----- PROFILE -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print("-------------------")