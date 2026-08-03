# ==============================
# Set 3 Solutions
# ==============================

# --------------------------------
# Question 1 — Secret Agent
# --------------------------------
def verify_code(code):
    if code == "007":
        return "Access Granted"
    return "Access Denied"


code = input("Enter code: ")
print(verify_code(code))

# --------------------------------
# Question 2 — Restaurant Discount
# --------------------------------
bill = float(input("\nEnter bill amount: "))

if bill >= 1000:
    bill *= 0.9

print("Final Bill:", bill)

# --------------------------------
# Question 3 — Username Strength
# --------------------------------
def check_username(username):
    if len(username) < 5:
        return "Weak"
    elif len(username) <= 10:
        return "Good"
    else:
        return "Strong"


username = input("\nEnter username: ")
print(check_username(username))

# --------------------------------
# Question 4 — Number Analyzer
# --------------------------------
number = int(input("\nEnter a number: "))

if number >= 0:
    print("Positive")
else:
    print("Negative")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# --------------------------------
# Question 5 — Smart Greeting
# --------------------------------
def greet(name):
    if name == "Radhika":
        return "Welcome back, Radhika!"
    return f"Hello, {name}"


name = input("\nEnter your name: ")
print(greet(name))


# --------------------------------
# Question 6 — Exam Result
# --------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    return "Fail"


marks = int(input("\nEnter marks: "))
print(calculate_grade(marks))


# --------------------------------
# Question 7 — Mini ATM
# --------------------------------
balance = float(input("\nEnter balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient Funds")
else:
    print("Remaining Balance:", balance - withdraw)


# --------------------------------
# Question 8 — Compare Numbers
# --------------------------------
def compare(a, b):
    if a > b:
        return "Greater"
    elif a < b:
        return "Smaller"
    return "Equal"


print(compare(10, 5))


# --------------------------------
# Question 9 — Leap Year
# --------------------------------
def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


year = int(input("\nEnter year: "))

if is_leap(year):
    print("Leap Year")
else:
    print("Not Leap Year")


# --------------------------------
# Question 10 — FizzBuzz Lite
# --------------------------------
number = int(input("\nEnter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


# --------------------------------
# Bonus Challenge — Login System
# --------------------------------
def login(username, password):
    if username == "admin" and password == "python123":
        return "Login Successful"
    return "Invalid Credentials"


username = input("\nUsername: ")
password = input("Password: ")

print(login(username, password))
