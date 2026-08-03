# Set 9: Modules, Random & Command-Line

This set introduces Python modules, random number generation, slicing, statistics, and command-line arguments.

## Topics Covered

- `random`
- `statistics`
- Slicing
- `sys.argv`
- Importing modules
- Creating your own Python library

---

# Question 1 — Dice Roller 🎲

## Problem

Generate a random number between **1 and 6**.

Example:

```text
You rolled: 4
```

Use:

- `random.randint()`

### Solution

```python
import random

roll = random.randint(1, 6)
print("You rolled:", roll)
```

---

# Question 2 — Coin Toss 🪙

## Problem

Randomly print either:

```text
Heads
```

or

```text
Tails
```

Use:

- `random.choice()`

### Solution

```python
import random

print(random.choice(["Heads", "Tails"]))
```

---

# Question 3 — Lucky Winner 🎉

## Problem

Given:

```python
participants = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul"
]
```

Randomly choose one winner.

Use:

- `random.choice()`

### Solution

```python
import random

participants = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul"
]

winner = random.choice(participants)
print("Winner:", winner)
```

---

# Question 4 — Student Statistics 📊

## Problem

Given:

```python
marks = [78, 90, 85, 92, 67, 88]
```

Print:

- Mean
- Median

Use the `statistics` module.

### Solution

```python
import statistics

marks = [78, 90, 85, 92, 67, 88]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
```

---

# Question 5 — Password Generator (Easy) 🔐

## Problem

Generate a **6-digit numeric password**.

Example:

```text
593108
```

Restriction:

- Don't hardcode six separate random numbers.

### Solution

```python
import random

password = random.randint(100000, 999999)

print(password)
```

---

# Question 6 — Secret Word

## Problem

Given:

```python
word = "Programming"
```

Print:

- First 4 letters
- Last 3 letters
- Every second character

Use slicing only.

### Solution

```python
word = "Programming"

print(word[:4])
print(word[-3:])
print(word[::2])
```

Example Output:

```text
Prog
ing
Pormig
```

---

# Question 7 — Name Formatter

## Problem

Given:

```python
names = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul"
]
```

Print only:

```text
Aman
Priya
Karan
```

Use slicing.

### Solution

```python
names = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul"
]

for name in names[1:4]:
    print(name)
```

---

# Question 8 — Simple Command-Line Program

## Problem

Create:

```text
hello.py
```

If the program is run as:

```bash
python hello.py Radhika
```

Output:

```text
Hello, Radhika!
```

If no name is given:

```text
Usage: python hello.py <name>
```

Use:

- `import sys`

### Solution

**hello.py**

```python
import sys

if len(sys.argv) > 1:
    print("Hello,", sys.argv[1] + "!")
else:
    print("Usage: python hello.py <name>")
```

---

# Question 9 — Create Your First Library 📦

## Problem

Create:

```text
calculator.py
```

with the following functions:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`

Then create:

```text
main.py
```

Import your library and use all three functions.

### Solution

**calculator.py**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

**main.py**

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
```

Example Output:

```text
15
5
50
```

---

# Question 10 — Random Quiz 🎮

## Problem

Store:

```python
questions = [
    "Capital of India?",
    "Largest planet?",
    "Fastest land animal?",
    "Python creator?"
]
```

Randomly choose one question and print it.

### Solution

```python
import random

questions = [
    "Capital of India?",
    "Largest planet?",
    "Fastest land animal?",
    "Python creator?"
]

print(random.choice(questions))
```

Example Output:

```text
Largest planet?
```

---

# ⭐ Bonus Challenge — Create Your First Library

Create a file named:

```text
utilities.py
```

It should contain:

- `is_even(n)`
- `square(n)`
- `cube(n)`

Import it into another Python file and test all three functions.

### Solution

**utilities.py**

```python
def is_even(n):
    return n % 2 == 0

def square(n):
    return n ** 2

def cube(n):
    return n ** 3
```

**test.py**

```python
import utilities

print(utilities.is_even(8))
print(utilities.square(5))
print(utilities.cube(3))
```

Example Output:

```text
True
25
27
```

---

## Concepts Practiced

- Importing modules
- Creating your own modules
- `random.randint()`
- `random.choice()`
- `statistics.mean()`
- `statistics.median()`
- String slicing
- List slicing
- `sys.argv`
- Organizing Python code into reusable libraries
