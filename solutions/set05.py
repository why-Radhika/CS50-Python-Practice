# ==============================
# Set 5 Solutions
# ==============================

# Question 1 — Count to N (using while loop)

n = int(input("Enter a number: "))

if n <= 0:
    print("Invalid Input")
else:
    i = 1
    while i <= n:
        print(i)
        i += 1


# Question 1 — Count to N (using for loop)

n = int(input("\nEnter a number: "))

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1, n + 1):
        print(i)


# Question 2 — Sum of First N Numbers (using while loop)

n = int(input("\nEnter a number: "))

if n <= 0:
    print("Invalid Input")
else:
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    print("Sum =", total)


# Question 2 — Sum of First N Numbers (using for loop)

n = int(input("\nEnter a number: "))

if n <= 0:
    print("Invalid Input")
else:
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum =", total)


# Question 3 — Even Numbers (Method 1)

for i in range(2, 51, 2):
    print(i)


# Question 3 — Even Numbers (Method 2)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# Question 4 — Shopping List

shopping = ["Milk", "Bread", "Eggs", "Butter"]

for count, item in enumerate(shopping, start=1):
    print(f"{count}. {item}")


# Question 5 — Student Marks

marks = {
    "Riya": 90,
    "Rahul": 82,
    "Anjali": 95,
    "Karan": 76
}

name = input("\nEnter the student's name: ").strip().title()

if name in marks:
    print("Marks:", marks[name])
else:
    print("Student not found")


# Question 6 — Multiplication Table

number = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Question 7 — Password Attempts

password = "python123"
attempts = 0

while attempts < 3:
    user_password = input("Enter the password: ")

    if user_password == password:
        print("Access Granted")
        break

    attempts += 1

    if attempts == 3:
        print("Account Locked")
    else:
        print("Incorrect Password. Try Again.")


# Question 8 — Grocery Bill

prices = {
    "Rice": 60,
    "Milk": 30,
    "Bread": 40,
    "Eggs": 80
}

item = input("\nEnter the item: ").strip().title()
quantity = int(input("Enter quantity: "))

if quantity <= 0:
    print("Invalid quantity")
elif item in prices:
    print("Total =", prices[item] * quantity)
else:
    print("Item not available")


# Question 9 — Number Guessing Game

secret_number = 7

while True:
    guess = int(input("\nGuess the number: "))

    if guess == secret_number:
        print("Congratulations!")
        break
    else:
        print("Try Again")


# Question 10 — Mini Menu (Challenge)

def hello():
    print("Hello!")


def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 + num2


while True:
    option = int(input("\n1. Say Hello\n2. Add Two Numbers\n3. Exit\n\nChoose an option: "))

    if option == 1:
        hello()

    elif option == 2:
        print("Sum =", add())

    elif option == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")


# ⭐ Bonus Challenge — Student Report Card

def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)
    print(f"Average = {average:.2f}")


students = {
    "Radhika": [90, 85, 88],
    "Aman": [78, 82, 80],
    "Priya": [95, 91, 97]
}

name = input("\nEnter the student's name: ").strip().title()

if name in students:
    print("Marks:", students[name])
    calculate_average(students[name])
else:
    print("Student not found")
