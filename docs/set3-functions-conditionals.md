# Set 3: Functions + Conditionals

This set combines functions and conditional statements to build reusable programs and strengthen problem-solving skills.

## Topics Covered

- Functions
- Parameters
- Return values
- if
- elif
- else
- String comparison
- len()
- Arithmetic operators
- Modulo operator (%)
- Boolean values
- Logical operators (`and`)

---

# Question 1 — Secret Agent

## Problem

Create a function:

```python
def verify_code(code):
```

Return:

- `"Access Granted"` if the code is `"007"`
- `"Access Denied"` otherwise.

### Example

```
Enter code: 007
Access Granted
```

## Concepts

- Functions
- Parameters
- Return values
- Strings
- if/else

---

# Question 2 — Restaurant Discount

## Problem

Ask the user for the bill amount.

Rules:

- Bill ≥ 1000 → Apply a 10% discount.
- Otherwise → No discount.

### Example

```
Bill: 1200
Final Bill: 1080
```

## Concepts

- float
- if
- Arithmetic

---

# Question 3 — Username Strength Checker

## Problem

Create:

```python
def check_username(username):
```

Return:

- `"Weak"` if length is less than 5
- `"Good"` if length is between 5 and 10
- `"Strong"` if length is greater than 10

### Example

```
Enter username: radhika123
Strong
```

## Concepts

- Functions
- len()
- if/elif/else

---

# Question 4 — Number Analyzer

## Problem

Ask the user for a number.

Print whether it is:

- Positive or Negative
- Even or Odd

### Example

```
Enter number: -8

Negative
Even
```

## Concepts

- Modulo operator
- Multiple conditionals

---

# Question 5 — Smart Greeting

## Problem

Create:

```python
def greet(name):
```

If the name is `"Radhika"` return:

```
Welcome back, Radhika!
```

Otherwise return:

```
Hello, <name>
```

### Example

```
Enter name: Rahul
Hello, Rahul
```

## Concepts

- Functions
- Strings
- if

---

# Question 6 — Exam Result Calculator

## Problem

Create:

```python
def calculate_grade(marks):
```

Rules:

- 90+ → A
- 80–89 → B
- 70–79 → C
- Below 70 → Fail

Return the grade.

### Example

```python
grade = calculate_grade(92)
print(grade)
```

Output

```
A
```

## Concepts

- Functions
- Return values
- if/elif/else

---

# Question 7 — Mini ATM

## Problem

Ask the user for:

- Balance
- Withdrawal amount

If the withdrawal amount exceeds the balance, print:

```
Insufficient Funds
```

Otherwise print the remaining balance.

### Example

```
Balance: 5000
Withdraw: 1200

Remaining Balance: 3800
```

## Concepts

- Arithmetic
- if/else

---

# Question 8 — Number Comparison Challenge

## Problem

Create:

```python
def compare(a, b):
```

Return:

- `"Greater"`
- `"Smaller"`
- `"Equal"`

### Example

```python
print(compare(10, 5))
```

Output

```
Greater
```

## Concepts

- Functions
- Comparison operators
- if/elif/else

---

# Question 9 — Leap Year Checker Function

## Problem

Create:

```python
def is_leap(year):
```

Return:

- `True`
- `False`

Then use the function to print:

```
Leap Year
```

or

```
Not Leap Year
```

### Example

```
Enter year: 2024

Leap Year
```

## Concepts

- Boolean values
- Functions
- Conditionals

---

# Question 10 — FizzBuzz Lite (Challenge)

## Problem

Ask the user for a number.

Rules:

- Divisible by both 3 and 5 → `"FizzBuzz"`
- Divisible by 3 → `"Fizz"`
- Divisible by 5 → `"Buzz"`
- Otherwise print the number.

### Example

```
15 → FizzBuzz
9 → Fizz
10 → Buzz
7 → 7
```

**Hint:** Check divisibility by both numbers first.

## Concepts

- Modulo operator
- Multiple conditions
- Order of evaluation

---

# ⭐ Bonus Challenge — Login System

## Problem

Create:

```python
def login(username, password):
```

Use:

- Username: `"admin"`
- Password: `"python123"`

Return:

```
Login Successful
```

only if both are correct.

Otherwise return:

```
Invalid Credentials
```

### Example

```
Username: admin
Password: python123

Login Successful
```

## Concepts

- Functions
- String comparison
- Logical operator (`and`)
- Return values
