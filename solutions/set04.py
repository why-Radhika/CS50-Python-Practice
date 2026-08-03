# ==============================
# Set 4 Solutions
# ==============================

# Project 1 — Coffee Shop ☕

def bill(coffee, large):
    if coffee == "Espresso":
        total = 120
    elif coffee == "Latte":
        total = 180
    elif coffee == "Cappuccino":
        total = 200
    else:
        return None

    if large == "yes":
        total += 40

    return total


def member_bill(total):
    return total * 0.90


coffee = input("Hey, Would you like some coffee? (Espresso/Latte/Cappuccino): ")
coffee = coffee.strip().title()

large = input("Would you like a large cup? (yes/no): ")
large = large.strip().lower()

member = input("Are you a member? (yes/no): ")
member = member.strip().lower()

total = bill(coffee, large)

if total is None:
    print("Invalid coffee selection.")
elif member == "yes":
    print(f"Final Bill: ₹{member_bill(total):.2f}")
else:
    print(f"Final Bill: ₹{total:.2f}")


# Project 2 — Simple Login System 🔐

def credentials(username, password):
    actual_username = "admin"
    actual_password = "python123"

    if username == actual_username and password == actual_password:
        return "Welcome Admin"
    elif username != actual_username:
        return "Unknown User"
    else:
        return "Incorrect Password"


username = input("Enter your username: ")
password = input("Enter your password: ")

print(credentials(username, password))


# Project 3 — BMI Calculator 🏃

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        print("Invalid Response")
        return None
    else:
        return weight / (height ** 2)


def classify_bmi(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Normal"
    elif 25 <= BMI < 30:
        return "Overweight"
    else:
        return "Obese"


weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))

BMI = calculate_bmi(weight, height)

if BMI is not None:
    print(f"Your BMI is: {BMI:.2f}")
    print(f"You are {classify_bmi(BMI)}")


# Project 4 — Electricity Bill ⚡

def calculate_bill(units):
    if units <= 0:
        print("Invalid Response")
        return None

    if units < 100:
        return units * 5
    elif units <= 300:
        return units * 7
    else:
        return units * 10


def apply_discount(total_bill):
    if total_bill > 2000:
        return total_bill - 200
    return total_bill


units = int(input("Enter the units consumed: "))

total_bill = calculate_bill(units)

if total_bill is not None:
    final_bill = apply_discount(total_bill)

    print("Units consumed:", units)
    print("Total Bill: ₹", total_bill)

    if total_bill > 2000:
        print("Discount: ₹200")
    else:
        print("Discount: ₹0")

    print("Final Bill: ₹", final_bill)


# Project 5 — Restaurant Ordering 🍕

def calculate_bill(food, quantity):
    if quantity <= 0:
        print("Invalid Response")
        return None

    if food == "Pizza":
        total_bill = 300 * quantity
    elif food == "Burger":
        total_bill = 180 * quantity
    elif food == "Pasta":
        total_bill = 220 * quantity
    else:
        return None

    return total_bill


def discount(total_bill):
    return total_bill - (total_bill * 0.15)


food = input("What would you like to have? (Pizza/Burger/Pasta): ")
food = food.strip().title()

quantity = int(input("How many of those would you like? "))

total_bill = calculate_bill(food, quantity)

if total_bill is None:
    print("Invalid food selection.")
elif quantity >= 5:
    print(f"Final Bill: ₹{discount(total_bill):.2f}")
else:
    print(f"Final Bill: ₹{total_bill:.2f}")


# 🌟 Bonus Project — Bank ATM

initial_balance = 5000

action = input("Hello, How may I help you today? (Withdraw, Deposit, Check Balance): ")
action = action.strip().title()

if action == "Withdraw":
    amount = float(input("How much amount would you like to withdraw? "))

    if amount > initial_balance:
        print("You do not have enough balance!")
    else:
        print("Your amount is withdrawn, your remaining balance is", initial_balance - amount)

elif action == "Deposit":
    amount = float(input("Enter the amount you want to deposit: "))
    print("Your amount has been deposited. Your current balance is", initial_balance + amount)

elif action == "Check Balance":
    print("Your current balance is", initial_balance)

else:
    print("Invalid option.")
