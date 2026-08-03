# Set 6: Mini Projects

This project set combines everything you've learned so far—functions, conditionals, loops, lists, and dictionaries—to build small real-world applications.

## Topics Covered

- Functions
- Loops
- Lists
- Dictionaries
- Menu-driven programs
- Nested dictionaries/lists
- Program design
- User input validation
- Arithmetic
- Multiple functions working together

---

# Project 1 — Coffee Shop POS ☕

## Problem

You're the cashier at a coffee shop.

### Menu

| Coffee | Price |
|---------|------:|
| Espresso | ₹120 |
| Latte | ₹180 |
| Cappuccino | ₹200 |

### Requirements

- Display the menu.
- Ask the customer to choose a coffee.
- Ask for quantity.
- Ask whether they are a member.
- Calculate the total bill.
- Members receive a **10% discount**.
- Print a receipt.

### Example

```
========= RECEIPT =========

Coffee    : Latte
Quantity  : 3
Subtotal  : ₹540
Discount  : ₹54
Final Bill: ₹486

===========================
```

Use:

- Dictionary
- Loop (for validation)
- Functions

---

# Project 2 — Student Report System 🎓

## Problem

Store:

```python
students = {
    "Radhika": [90, 85, 88],
    "Aman": [78, 82, 80],
    "Priya": [95, 91, 97],
    "Karan": [60, 65, 70]
}
```

For a selected student print:

- Marks
- Average
- Highest Mark
- Lowest Mark
- Result (Pass/Fail)

### Rule

If **any** subject is below **35**

```
Fail
```

Otherwise

```
Pass
```

### Restrictions

Do **not** use:

- sum()
- max()
- min()

Use loops instead.

---

# Project 3 — Grocery Store 🛒

## Problem

Menu

| Item | Price |
|------|------:|
| Rice | ₹60 |
| Milk | ₹30 |
| Bread | ₹40 |
| Eggs | ₹80 |

The customer can continue buying until they type:

```
done
```

Finally print:

- Items Purchased
- Grand Total
- Total Items

Use:

- while loop
- Dictionary
- Functions

---

# Project 4 — ATM Simulator 🏧

## Problem

Initial balance:

```
₹5000
```

Display the menu repeatedly:

```
1. Withdraw
2. Deposit
3. Check Balance
4. Exit
```

### Rules

Withdraw

- Cannot withdraw more than the available balance.
- Cannot withdraw zero or negative amounts.

Deposit

- Cannot deposit zero or negative amounts.

Use functions wherever appropriate.

---

# Project 5 — Quiz Game 🎮

## Problem

Create a quiz with **5 questions**.

Example:

```
Capital of India?

A Delhi
B Mumbai
C Chennai
D Jaipur
```

The user enters:

```
A
```

At the end print:

- Score
- Correct Answers
- Wrong Answers

### Bonus

Display:

- Excellent
- Good
- Needs Practice

based on the final score.

---

# ⭐ Bonus Challenge — Expense Tracker

## Problem

Display the menu:

```
1. Add Expense
2. Show Total
3. Show All Expenses
4. Exit
```

When adding expenses:

```
Food 250
Travel 100
Books 500
```

Choosing **Show Total** should display:

```
₹850
```

Choosing **Show All Expenses** should display:

```
Food : ₹250
Travel : ₹100
Books : ₹500
```

---

## Restrictions

For this project set, **do not use**:

- sum()
- max()
- min()
- list comprehensions
- try/except

Focus on strengthening your loop logic first.
