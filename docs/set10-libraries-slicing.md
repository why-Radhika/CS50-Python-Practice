# Set 10: Modules + Random + Statistics + Slicing

Difficulty: ⭐⭐☆☆☆ → ⭐⭐⭐☆☆

This challenge set combines everything you've learned so far, including functions, lists, dictionaries, loops, exceptions, randomization, statistics, slicing, and creating your own Python modules.

## Topics Covered

- Functions
- Lists
- Dictionaries
- Loops
- Exceptions
- `random`
- `statistics`
- Slicing
- Modules

---

# Question 1 — Roll Until Six 🎲

## Problem

Keep rolling a die until you get **6**.

Example:

```text
You rolled: 2
You rolled: 5
You rolled: 1
You rolled: 6
You won!
```

Use:

- `random.randint()`
- `while`

### Solution

```python
import random

while True:
    roll = random.randint(1, 6)
    print("You rolled:", roll)

    if roll == 6:
        print("You won!")
        break
```

---

# Question 2 — Lucky Student 🎓

## Problem

Given:

```python
students = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul",
    "Neha"
]
```

Randomly choose **3 unique winners**.

Restriction:

- A student cannot win twice.

### Solution

```python
import random

students = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul",
    "Neha"
]

winners = random.sample(students, 3)

for winner in winners:
    print(winner)
```

---

# Question 3 — Student Analytics 📊

## Problem

Given:

```python
marks = [92, 78, 85, 95, 67, 88, 73]
```

Print:

- Highest
- Lowest
- Mean
- Median
- Range

Use the `statistics` module where appropriate.

### Solution

```python
import statistics

marks = [92, 78, 85, 95, 67, 88, 73]

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Range:", max(marks) - min(marks))
```

---

# Question 4 — Username Formatter

## Problem

Ask the user for a username.

Example input:

```text
RadhikaGupta2003
```

Print:

- First 5 characters
- Last 4 characters
- Username length

Use slicing.

### Solution

```python
username = input("Enter username: ")

print("First 5 characters:", username[:5])
print("Last 4 characters:", username[-4:])
print("Username length:", len(username))
```

---

# Question 5 — Random Password Generator 🔐

## Problem

Generate an **8-character password**.

Allowed characters:

```python
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
```

The password should contain a random mix of letters and numbers.

Restriction:

- Don't hardcode each position.

### Solution

```python
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

characters = letters + numbers

password = ""

for _ in range(8):
    password += random.choice(characters)

print(password)
```

---

# Question 6 — Playlist Shuffle 🎵

## Problem

Given:

```python
songs = [
    "Believer",
    "Perfect",
    "Skyfall",
    "Shape of You",
    "Bones"
]
```

Randomly shuffle the playlist.

Then print the songs in the new order.

### Solution

```python
import random

songs = [
    "Believer",
    "Perfect",
    "Skyfall",
    "Shape of You",
    "Bones"
]

random.shuffle(songs)

for song in songs:
    print(song)
```

---

# Question 7 — Mini Statistics App

## Problem

Ask the user how many numbers they want to enter.

Example:

```text
How many? 5
```

Accept those numbers into a list.

Finally print:

- Mean
- Median
- Highest
- Lowest

### Solution

```python
import statistics

count = int(input("How many numbers? "))

numbers = []

for _ in range(count):
    numbers.append(float(input("Enter number: ")))

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Highest:", max(numbers))
print("Lowest:", min(numbers))
```

---

# Question 8 — Build Your Own Utility Library 📦

## Problem

Create:

```text
math_utils.py
```

with functions:

- `average(numbers)`
- `highest(numbers)`
- `lowest(numbers)`

Do **not** use the `statistics` module inside your library.

Then import the library into another file and test it.

### Solution

**math_utils.py**

```python
def average(numbers):
    return sum(numbers) / len(numbers)

def highest(numbers):
    return max(numbers)

def lowest(numbers):
    return min(numbers)
```

**main.py**

```python
import math_utils

numbers = [10, 20, 30, 40, 50]

print(math_utils.average(numbers))
print(math_utils.highest(numbers))
print(math_utils.lowest(numbers))
```

---

# Question 9 — String Slicing Challenge

## Problem

Given:

```python
sentence = "Python Programming"
```

Print:

```text
Python
Programming
Pto rgamn
gnimmargorP nohtyP
```

Use slicing only.

### Solution

```python
sentence = "Python Programming"

print(sentence[:6])
print(sentence[7:])
print(sentence[::2])
print(sentence[::-1])
```

---

# Question 10 — Number Lottery 🎰

## Problem

Generate **6 unique random numbers** between **1 and 50**.

Example:

```text
4
17
21
29
33
48
```

No duplicates allowed.

### Solution

```python
import random

numbers = random.sample(range(1, 51), 6)

for number in sorted(numbers):
    print(number)
```

---

# ⭐ Bonus Project — Student Performance Analyzer

## Problem

Given:

```python
students = {
    "Radhika": [90, 85, 88],
    "Aman": [70, 60, 80],
    "Priya": [95, 91, 97],
    "Karan": [50, 45, 55]
}
```

For each student:

- Calculate average.
- Print the highest score.
- Print the lowest score.
- Decide:
  - Average ≥ 90 → Excellent
  - Average ≥ 75 → Good
  - Otherwise → Needs Improvement

Try to organize your solution into functions.

### Solution

```python
def average(scores):
    return sum(scores) / len(scores)

def performance(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 75:
        return "Good"
    else:
        return "Needs Improvement"

students = {
    "Radhika": [90, 85, 88],
    "Aman": [70, 60, 80],
    "Priya": [95, 91, 97],
    "Karan": [50, 45, 55]
}

for name, scores in students.items():
    avg = average(scores)

    print(f"\n{name}")
    print("Average:", avg)
    print("Highest:", max(scores))
    print("Lowest:", min(scores))
    print("Performance:", performance(avg))
```

---

# Concepts Practiced

- `random.randint()`
- `random.choice()`
- `random.sample()`
- `random.shuffle()`
- `statistics.mean()`
- `statistics.median()`
- String slicing
- List slicing
- Functions
- Dictionaries
- Creating custom modules
- Organizing code into reusable functions
- Working with loops and collections
