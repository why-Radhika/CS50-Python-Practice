# ==========================================
# Set 2: Conditionals (Lecture 1)
# ==========================================

# -------------------------
# Question 1
# Positive, Negative, or Zero
# -------------------------

num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# -------------------------
# Question 2
# Even or Odd
# -------------------------

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# -------------------------
# Question 3
# Voting Eligibility
# -------------------------

age = int(input("Age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# -------------------------
# Question 4
# Password Checker
# -------------------------

password = "python123"

user_password = input("Enter password: ")

if user_password == password:
    print("Access Granted")
else:
    print("Access Denied")


# -------------------------
# Question 5
# Largest of Two Numbers
# -------------------------

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 > num2:
    print(num1, "is larger")
elif num2 > num1:
    print(num2, "is larger")
else:
    print("Both numbers are equal")


# -------------------------
# Question 6
# Grade Calculator
# -------------------------

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# -------------------------
# Question 7
# Leap Year Lite
# -------------------------

year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")


# -------------------------
# Question 8
# Movie Ticket Price
# -------------------------

age = int(input("Enter age: "))

if age < 12:
    print("Ticket Price: ₹100")
elif age < 60:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹150")


# -------------------------
# Question 9
# Username Validation
# -------------------------

username = input("Enter username: ")

if len(username) < 5:
    print("Username too short")
else:
    print("Valid username")


# -------------------------
# Question 10
# Mini Calculator (Challenge)
# -------------------------

num1 = int(input("First number: "))
operator = input("Operator (+, -, *, /): ")
num2 = int(input("Second number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")
