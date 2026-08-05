
# Set 12 — Unit Testing Fundamentals 🧪

This set introduces **Unit Testing** in Python using **pytest**.  
For every question:

- Write the function in one file (e.g. `calculator.py`)
- Write the tests in another file (e.g. `test_calculator.py`)
- Use `pytest`
- Use `assert` statements

---

# Topics Covered

- Functions
- Unit Testing
- `pytest`
- Assertions
- Boundary Testing
- String methods
- Lists
- Boolean logic
- Test-Driven Development (TDD)

---

# Question 1 — Square Function 🔢

## Problem

Create:

```python
def square(n):
    ...
```

### Test Cases

| Input | Expected Output |
|--------|-----------------|
| 2 | 4 |
| 5 | 25 |
| -3 | 9 |
| 0 | 0 |

---

# Question 2 — Even Number Checker ✅

## Problem

Create:

```python
def is_even(n):
    ...
```

Return:

- `True`
- `False`

### Test Cases

- `2`
- `7`
- `0`
- `-4`

---

# Question 3 — Grade Calculator 🎓

## Problem

Create:

```python
def grade(score):
    ...
```

### Rules

| Score | Grade |
|-------|-------|
| 90+ | A |
| 80–89 | B |
| 70–79 | C |
| Below 70 | D |

### Test Cases

- 95
- 90
- 89
- 80
- 70
- 45

> **Pay special attention to boundary values.**

---

# Question 4 — Username Formatter 👤

## Problem

Create:

```python
def format_username(name):
    ...
```

### Requirements

- Remove leading/trailing spaces
- Convert to Title Case

Example

```text
"  radhika  "
        ↓
"Radhika"
```

### Test Cases

- Extra spaces
- Already formatted
- ALL UPPERCASE
- Empty string

---

# Question 5 — Reverse String 🔄

## Problem

Create:

```python
def reverse(text):
    ...
```

Example

```text
Python
   ↓
nohtyP
```

### Test Cases

- Normal word
- Empty string
- One character
- Palindrome

---

# Question 6 — Count Vowels 🔤

## Problem

Create:

```python
def count_vowels(text):
    ...
```

Example

```text
apple
  ↓
2
```

### Test Cases

- `"apple"`
- Empty string
- No vowels
- Uppercase vowels

---

# Question 7 — Average Calculator 📊

## Problem

Create:

```python
def average(numbers):
    ...
```

### Test Cases

- `[1, 2, 3]`
- `[10]`
- `[5, 5, 5]`

Think about what should happen with an empty list.

Choose a behavior (return `0`, `None`, or raise an exception) and write tests for it.

---

# Question 8 — Password Validator 🔐

## Problem

Create:

```python
def valid_password(password):
    ...
```

### Rule

Password must contain **at least 8 characters**.

Return:

- `True`
- `False`

### Test Cases

- Exactly 8 characters
- 7 characters
- Long password
- Empty string

---

# ⭐ Bonus Challenge — Test First (TDD)

Create:

```python
def is_palindrome(text):
    ...
```

### Instructions

1. Write **all the tests first**.
2. Run the tests (they should fail).
3. Implement the function.
4. Keep improving it until **all tests pass**.

This introduces **Test-Driven Development (TDD)**, a common professional software development practice.

---

# Submission Structure

```text
set12/
│
├── question1/
│   ├── square.py
│   └── test_square.py
│
├── question2/
│   ├── even.py
│   └── test_even.py
│
├── question3/
│   ├── grade.py
│   └── test_grade.py
│
├── ...
│
└── question8/
    ├── password.py
    └── test_password.py
```

---

Happy Testing! 🚀
