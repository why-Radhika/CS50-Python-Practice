# ==============================
# Set 6 Solutions
# ==============================

# Project 1 — Coffee Shop POS ☕

def calculate_bill(menu, coffee, quantity):
    return menu[coffee] * quantity


def discounted(total_bill):
    return total_bill * 0.10


menu = {
    "Espresso": 120,
    "Latte": 180,
    "Cappuccino": 200
}

print("MENU")
for coffee in menu:
    print(f"{coffee}: ₹{menu[coffee]}")

while True:
    coffee = input("Which coffee would you like to order? ").strip().title()
    if coffee in menu:
        break
    print("Invalid coffee selection.")

while True:
    quantity = int(input("How many would you like? "))
    if quantity > 0:
        break
    print("Invalid quantity.")

member = input("Are you a member? (Yes/No): ").strip().title()

total_bill = calculate_bill(menu, coffee, quantity)

if member == "Yes":
    discount = discounted(total_bill)
else:
    discount = 0

final_bill = total_bill - discount

print("\n========= RECEIPT =========")
print(f"Coffee    : {coffee}")
print(f"Quantity  : {quantity}")
print(f"Subtotal  : ₹{total_bill:.2f}")
print(f"Discount  : ₹{discount:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")
print("===========================")


# Project 2 — Student Report System 🎓

def calculate_average(marks):
    total = 0
    count = 0

    for score in marks:
        total += score
        count += 1

    return total / count


def highest_marks(marks):
    highest = marks[0]

    for score in marks:
        if score > highest:
            highest = score

    return highest


def lowest_marks(marks):
    lowest = marks[0]

    for score in marks:
        if score < lowest:
            lowest = score

    return lowest


def final_result(marks):
    for score in marks:
        if score < 35:
            return "Fail"

    return "Pass"


students = {
    "Radhika": [90, 85, 88],
    "Aman": [78, 82, 80],
    "Priya": [95, 91, 97],
    "Karan": [60, 34, 70]
}

name = input("\nEnter student name: ").strip().title()

if name in students:
    marks = students[name]

    print("Marks:", marks)
    print("Average:", calculate_average(marks))
    print("Highest:", highest_marks(marks))
    print("Lowest:", lowest_marks(marks))
    print("Result:", final_result(marks))
else:
    print("Invalid Name")


# Project 3 — Grocery Store 🛒

def total_bill(order_list, prices):
    total = 0

    for item in order_list:
        total += order_list[item] * prices[item]

    return total


def total_quantity(order_list):
    total = 0

    for item in order_list:
        total += order_list[item]

    return total


prices = {
    "Rice": 60,
    "Milk": 30,
    "Bread": 40,
    "Eggs": 80
}

order_list = {}

while True:
    item = input("\nWhat would you like to buy? (Done to finish): ").strip().title()

    if item == "Done":
        break

    if item not in prices:
        print("Invalid item.")
        continue

    quantity = int(input("Quantity: "))

    if quantity <= 0:
        print("Invalid quantity.")
        continue

    if item in order_list:
        order_list[item] += quantity
    else:
        order_list[item] = quantity

print("\nItems Purchased:")

for item in order_list:
    print(f"{item} x {order_list[item]}")

print("\nGrand Total: ₹", total_bill(order_list, prices))
print("Total Items:", total_quantity(order_list))


# Project 4 — ATM Simulator 🏧

current_balance = 5000


def action_withdraw(current_balance):
    amount = int(input("Enter amount to withdraw: "))

    if amount > current_balance:
        print("Not Enough Balance")
        return current_balance

    elif amount <= 0:
        print("Enter a valid amount")
        return current_balance

    return current_balance - amount


def action_deposit(current_balance):
    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Enter a valid amount")
        return current_balance

    return current_balance + amount


while True:
    action = int(input("\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Exit\n\nChoose: "))

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
        print("Invalid Input")


# Project 5 — Quiz Game 🎮

quiz = [
    {
        "question": "Capital of India?",
        "options": {
            "A": "Delhi",
            "B": "Mumbai",
            "C": "Chennai",
            "D": "Jaipur"
        },
        "answer": "A"
    },
    {
        "question": "Fastest Land Animal?",
        "options": {
            "A": "Lion",
            "B": "Cheetah",
            "C": "Tiger",
            "D": "Elephant"
        },
        "answer": "B"
    },
    {
        "question": "Who plays Spider-Man in the MCU?",
        "options": {
            "A": "Tom Cruise",
            "B": "Robert Downey Jr.",
            "C": "Tom Hanks",
            "D": "Tom Holland"
        },
        "answer": "D"
    },
    {
        "question": "Which is not a primary colour?",
        "options": {
            "A": "Red",
            "B": "Yellow",
            "C": "Pink",
            "D": "Green"
        },
        "answer": "C"
    },
    {
        "question": "Who wrote Harry Potter?",
        "options": {
            "A": "Arundhati Roy",
            "B": "J.K. Rowling",
            "C": "Rebecca Yarros",
            "D": "J.R.R. Tolkien"
        },
        "answer": "B"
    }
]

score = 0

for question in quiz:
    print("\n" + question["question"])

    for option, text in question["options"].items():
        print(option, text)

    answer = input("Your answer: ").strip().upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("\nScore:", score)
print("Correct Answers:", score)
print("Wrong Answers:", len(quiz) - score)

if score >= 4:
    print("Excellent")
elif score == 3:
    print("Good")
else:
    print("Needs Practice")


# ⭐ Bonus Challenge — Expense Tracker

expenses = {}


def add_expense():
    name = input("Expense name: ").strip().title()
    amount = int(input("Amount: ₹"))

    if name in expenses:
        expenses[name] += amount
    else:
        expenses[name] = amount


def total_expense():
    total = 0

    for amount in expenses.values():
        total += amount

    return total


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for name, amount in expenses.items():
        print(f"{name}: ₹{amount}")


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Total")
    print("3. Show All Expenses")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_expense()

    elif option == "2":
        print("Total: ₹", total_expense())

    elif option == "3":
        show_expenses()

    elif option == "4":
        print("Thank you!")
        break

    else:
        print("Invalid option.")
