# ==============================
# Set 8 Solutions
# Exception Handling
# ==============================


# ------------------------------
# Question 1 — Safe Integer Input
# ------------------------------

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print(f"You entered {num}")


# ------------------------------
# Question 2 — Keep Asking
# ------------------------------

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print(f"Your age is {age}")
        break


# ------------------------------
# Question 3 — Positive Integer
# ------------------------------

while True:
    try:
        num = int(input("Enter a number: "))

        if num <= 0:
            print("Enter a positive number.")
            continue

    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print("Accepted")
        break


# ------------------------------
# Question 4 — Safe Division
# ------------------------------

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ValueError:
    print("Invalid input. Please enter integers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)


# ------------------------------
# Question 5 — Create Your Own Function
# ------------------------------

def get_integer():
    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            return num


num1 = get_integer()
num2 = get_integer()

print("Sum:", num1 + num2)


# ------------------------------
# Question 6 — Guess the Number
# ------------------------------

secret_number = 7

while True:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        if guess == secret_number:
            print("Congratulations!")
            break
        else:
            print("Try Again.")


# ------------------------------
# Question 7 — Menu Program
# ------------------------------

def get_integer():
    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            return num


while True:
    try:
        action = int(input(
            "\n1. Add\n2. Subtract\n3. Exit\n\nChoose an option: "
        ))

    except ValueError:
        print("Invalid choice. Enter a number.")

    else:
        if action == 1:
            num1 = get_integer()
            num2 = get_integer()
            print("Answer:", num1 + num2)

        elif action == 2:
            num1 = get_integer()
            num2 = get_integer()
            print("Answer:", num1 - num2)

        elif action == 3:
            break

        else:
            print("Enter a valid menu choice.")


# ------------------------------
# Question 8 — BMI Calculator
# ------------------------------

def calculate_bmi():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))

        except ValueError:
            print("Please enter numeric values.")
            continue

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.")
            continue

        return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


bmi = calculate_bmi()

print(f"Your BMI is: {bmi:.2f}")
print(f"You are {classify_bmi(bmi)}")


# ------------------------------
# Question 9 — Student Marks
# ------------------------------

def get_marks():
    while True:
        try:
            marks = int(input("Enter your marks: "))

        except ValueError:
            print("Please enter a proper value.")
            continue

        if marks < 0 or marks > 100:
            print("Enter a valid score.")
            continue

        return marks


print(f"You scored {get_marks()}")


# ------------------------------
# Question 10 — ATM
# ------------------------------

current_balance = 5000


def action_withdraw(balance):
    while True:
        try:
            amount = int(input("Enter amount to withdraw: "))

        except ValueError:
            print("Enter amount in integer format.")

        else:
            if amount > balance:
                print("Not enough balance.")
                return balance

            elif amount <= 0:
                print("Enter a valid amount.")
                return balance

            else:
                return balance - amount


def action_deposit(balance):
    while True:
        try:
            amount = int(input("Enter amount to deposit: "))

        except ValueError:
            print("Enter amount in integer format.")

        else:
            if amount <= 0:
                print("Enter a valid amount.")
                return balance

            else:
                return balance + amount


while True:
    try:
        action = int(input(
            "\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\n\nChoose: "
        ))

    except ValueError:
        print("Enter a correct menu choice.")

    else:
        if action == 1:
            current_balance = action_withdraw(current_balance)
            print("Current Balance:", current_balance)

        elif action == 2:
            current_balance = action_deposit(current_balance)
            print("Current Balance:", current_balance)

        elif action == 3:
            print("Current Balance:", current_balance)

        elif action == 4:
            print("Thank you!")
            break

        else:
            print("Invalid Input.")


# ------------------------------
# Bonus Challenge
# ------------------------------

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input.")


action = int(input(
    "What do you want to know about the user?\n"
    "1. Age\n"
    "2. Marks\n"
    "3. Salary\n\nChoose: "
))

if action == 1:
    age = get_int("Enter your age: ")
    print("The age of the user is", age)

elif action == 2:
    marks = get_int("Enter your marks: ")
    print("The marks of the user is", marks)

elif action == 3:
    salary = get_int("Enter your salary: ")
    print("The salary of the user is", salary)

else:
    print("Invalid Input.")