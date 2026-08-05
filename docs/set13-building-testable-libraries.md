# Set 13 — Building Testable Python Libraries 🧪📦

## Goal

For every project:

- Write the program.
- Write `pytest` tests.
- Separate them into files.

Example:

```text
project/
│
├── calculator.py
├── test_calculator.py
```

or

```text
school/
│
├── school_utils.py
├── test_school_utils.py
```

---

# Topics Covered

- Functions
- Modules
- pytest
- Assertions
- Lists
- Dictionaries
- String methods
- Edge cases
- Exception testing
- Library design
- Test-Driven Development (TDD)

---

# Question 1 — Test Your Math Library 📦

## Problem

Create:

```text
math_utils.py
```

### Functions

```python
def average(numbers):
    ...

def highest(numbers):
    ...

def lowest(numbers):
    ...
```

### Write tests for

#### average()

Normal cases

```python
[1, 2, 3]
[10]
```

Edge cases

```python
[]
[-5, -10]
```

#### highest()

Test:

- Positive numbers
- Negative numbers
- One element
- Duplicate values

#### lowest()

Test:

- Positive numbers
- Negative numbers
- One element
- Duplicate values

### Challenge

Decide how your functions should behave for an empty list.

Should they:

- Return a value?
- Raise an exception?

Write tests for whichever design you choose.

---

# Question 2 — School Report Library 🎓

## Problem

Create:

```text
school_utils.py
```

### Functions

```python
def grade(score):
    ...

def passed(score):
    ...
```

### Rules

| Score | Grade |
|--------|-------|
| 90+ | A |
| 80+ | B |
| 70+ | C |
| Below 70 | D |

`passed(score)` should return:

- `True`
- `False`

### Test

- Every grade boundary
- Pass/fail boundary
- Invalid scores *(optional)*

---

# Question 3 — String Utilities 📖

## Problem

Create:

```text
string_utils.py
```

### Functions

```python
def reverse(text):
    ...

def count_vowels(text):
    ...

def is_palindrome(text):
    ...
```

### Write thorough tests

Examples:

```python
reverse("")
reverse("A")

count_vowels("APPLE")
count_vowels("xyz")

is_palindrome("Kayak")
is_palindrome("Python")
is_palindrome("")
```

Think about:

- Empty strings
- One character
- Uppercase vs lowercase
- Words with no vowels
- Palindromes of different lengths

---

# Question 4 — Password Validator 🔐

## Problem

Create:

```python
def valid_password(password):
    ...
```

### Rules

- Minimum **8 characters**
- Maximum **18 characters**

Return:

- `True`
- `False`

### Test Cases

- 7 characters
- 8 characters
- 18 characters
- 19 characters
- Empty string

---

# Question 5 — Student Statistics 📊

## Problem

Create:

```python
def student_statistics(marks):
    ...
```

Return:

```python
{
    "average": ...,
    "highest": ...,
    "lowest": ...
}
```

Example:

```python
student_statistics([90, 80, 100])
```

Returns

```python
{
    "average": 90,
    "highest": 100,
    "lowest": 80
}
```

### Test Cases

- Normal list
- One element
- All values the same
- Negative numbers
- Empty list

---

# ⭐ Final Project — Expense Tracker (Testable Version)

## Problem

Create:

```text
expense_utils.py
```

### Functions

```python
def add_expense(expenses, category, amount):
    ...

def total_expense(expenses):
    ...

def highest_expense(expenses):
    ...
```

Example

```python
expenses = {
    "Food": 500,
    "Travel": 1200,
    "Shopping": 800
}
```

Write tests for every function.

Think about:

- Empty dictionary
- Duplicate category
- Zero amount
- Negative amount

---

# ⭐⭐ Bonus Challenge — Test the Bug 🐞

This is a Test-Driven Development challenge.

Given the function:

```python
def discount(price):
    if price > 1000:
        return price * 0.9
    return price
```

**Do not change the function yet.**

Instead:

- Write every test you can think of.

Examples:

```python
999
1000
1001
5000
0
negative numbers
```

After writing the tests, ask yourself:

> Is the function behaving exactly as the requirements intend?

Sometimes, writing comprehensive tests is what reveals hidden bugs or ambiguous requirements.

---

Happy Testing! 🚀
