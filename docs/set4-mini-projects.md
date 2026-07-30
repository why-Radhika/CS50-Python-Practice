# Set 4: Mini Projects

This set combines everything learned so far into beginner-friendly mini projects. Each project is designed to take around **10–20 minutes** and encourages breaking problems into smaller functions.

## Topics Covered

- Functions
- Parameters
- Return values
- Conditional statements
- User input
- Arithmetic
- String comparison
- Program design
- Multiple functions
- Simple real-world applications

---

# Project 1 — Coffee Shop ☕

## Problem

A coffee shop sells:

| Coffee | Price |
|---------|------:|
| Espresso | ₹120 |
| Latte | ₹180 |
| Cappuccino | ₹200 |

Ask the customer:

- Coffee
- Large size? (yes/no)
- Member? (yes/no)

### Rules

- Large size adds **₹40**
- Members receive a **10% discount**

Use at least **two functions**.

### Example

```
Coffee : Latte
Size : Large
Member : Yes

Final Bill : ₹198
```

## Concepts

- Functions
- Return values
- if/elif/else
- Arithmetic

---

# Project 2 — Simple Login System 🔐

## Problem

Correct credentials:

```
Username : admin
Password : python123
```

### Rules

- Wrong username → **Unknown User**
- Correct username but wrong password → **Incorrect Password**
- Both correct → **Welcome Admin**

Use functions that return values.

### Example

```
Username: admin
Password: python123

Welcome Admin
```

## Concepts

- Functions
- String comparison
- Logical operators
- Return values

---

# Project 3 — BMI Calculator 🏃

## Problem

Ask the user for:

- Weight (kg)
- Height (m)

Calculate BMI using:

```
BMI = weight / height²
```

Then classify:

| BMI | Category |
|------|----------|
| Below 18.5 | Underweight |
| 18.5–24.9 | Normal |
| 25–29.9 | Overweight |
| 30+ | Obese |

Create two functions:

```python
calculate_bmi()

classify_bmi()
```

### Example

```
Weight: 65
Height: 1.70

BMI: 22.49
Normal
```

## Concepts

- Functions
- Arithmetic
- Floating-point numbers
- if/elif/else

---

# Project 4 — Electricity Bill ⚡

## Problem

Calculate the electricity bill using the following rates:

| Units | Rate |
|-------|------|
| Below 100 | ₹5/unit |
| 100–300 | ₹7/unit |
| Above 300 | ₹10/unit |

### Extra Rule

If the total bill exceeds **₹2000**, give a **₹200 discount**.

Print:

- Units
- Bill
- Discount
- Final Bill

### Example

```
Units: 350

Bill: ₹3500
Discount: ₹200
Final Bill: ₹3300
```

## Concepts

- Functions
- Arithmetic
- Conditional statements

---

# Project 5 — Restaurant Ordering 🍕

## Problem

Menu:

| Food | Price |
|------|------:|
| Pizza | ₹300 |
| Burger | ₹180 |
| Pasta | ₹220 |

Ask the user for:

- Food item
- Quantity

### Rule

If the quantity is **5 or more**, give a **15% discount**.

Return the final bill.

### Example

```
Food: Pizza
Quantity: 5

Final Bill: ₹1275
```

## Concepts

- Functions
- Arithmetic
- if/else

---

# ⭐ Bonus Project — Bank ATM

## Problem

Initial balance:

```
₹5000
```

Ask the user to choose one operation:

- Withdraw
- Deposit
- Check Balance

### Rules

#### Withdraw

- Ask for the amount.
- Prevent overdraft.
- Update the balance.

#### Deposit

- Add the amount to the balance.

#### Check Balance

- Display the current balance.

> **Note:** No loops are required. The program performs one operation and exits.

## Concepts

- Functions (optional)
- Conditionals
- Arithmetic
- Program flow
