# Set 11: Functions, Dictionaries & Mini Projects

Difficulty: ⭐⭐⭐☆☆

This set brings together functions, dictionaries, modules, randomization, loops, exceptions, and basic text processing into larger Python programs.

## Topics Covered

- Functions
- Dictionaries
- Lists
- Loops
- Exceptions
- `random`
- Modules
- String methods
- Slicing
- Mini projects

---

# Question 1 — Student Dashboard 📊

## Problem

Given:

```python
students = {
    "Radhika": [90, 88, 95],
    "Aman": [70, 82, 76],
    "Priya": [98, 96, 99],
    "Karan": [45, 60, 55]
}
```

Display for every student:

- Average
- Highest
- Lowest
- Grade

Grades:

```text
90+  -> A
80+  -> B
70+  -> C
else -> D
```

Use functions.

### Solution

```python
def average(scores):
    return sum(scores) / len(scores)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

students = {
    "Radhika": [90, 88, 95],
    "Aman": [70, 82, 76],
    "Priya": [98, 96, 99],
    "Karan": [45, 60, 55]
}

for name, marks in students.items():
    avg = average(marks)

    print("\nStudent:", name)
    print("Average:", avg)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    print("Grade:", grade(avg))
```

---

# Question 2 — Password Generator Pro 🔐

## Problem

Ask the user for the password length.

Example:

```text
Length: 12
```

Generate a random password using:

- Uppercase letters
- Lowercase letters
- Digits

Ignore symbols for now.

### Solution

```python
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

characters = letters + digits

length = int(input("Password length: "))

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Password:", password)
```

---

# Question 3 — Guess the Celebrity 🎲

## Problem

Given:

```python
celebrities = {
    "SRK": "Shah Rukh Khan",
    "MSD": "MS Dhoni",
    "VK": "Virat Kohli",
    "RDJ": "Robert Downey Jr."
}
```

Randomly choose one abbreviation.

Ask:

```text
Who is SRK?
```

Check whether the user's answer is correct.

### Solution

```python
import random

celebrities = {
    "SRK": "Shah Rukh Khan",
    "MSD": "MS Dhoni",
    "VK": "Virat Kohli",
    "RDJ": "Robert Downey Jr."
}

short = random.choice(list(celebrities.keys()))

answer = input(f"Who is {short}? ")

if answer.lower() == celebrities[short].lower():
    print("Correct!")
else:
    print("Wrong!")
    print("Answer:", celebrities[short])
```

---

# Question 4 — Your Own Statistics Library 📦

## Problem

Create:

```text
stats_utils.py
```

Functions:

- `average()`
- `highest()`
- `lowest()`
- `grade()`

Do **not** use the `statistics` module.

Use this library in another file.

### Solution

**stats_utils.py**

```python
def average(numbers):
    return sum(numbers) / len(numbers)

def highest(numbers):
    return max(numbers)

def lowest(numbers):
    return min(numbers)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"
```

**main.py**

```python
import stats_utils

marks = [90, 85, 92]

avg = stats_utils.average(marks)

print("Average:", avg)
print("Highest:", stats_utils.highest(marks))
print("Lowest:", stats_utils.lowest(marks))
print("Grade:", stats_utils.grade(avg))
```

---

# Question 5 — Mini Text Analyzer ✂️

## Problem

Input:

```text
Python Programming is Fun
```

Print:

- Characters
- Words
- First Word
- Last Word
- Reverse
- Every 2nd Character

### Solution

```python
text = input("Enter text: ")

words = text.split()

print("Characters:", len(text))
print("Words:", len(words))
print("First Word:", words[0])
print("Last Word:", words[-1])
print("Reverse:", text[::-1])
print("Every 2nd Character:", text[::2])
```

---

# ⭐ Final Project — Classroom Manager

## Problem

Store:

```python
students = {
    "Radhika": [90, 80, 95],
    "Aman": [70, 82, 78],
    "Priya": [99, 95, 97]
}
```

Create a menu:

```text
1. View Student
2. View Class Average
3. Pick Random Student
4. Exit
```

### Requirements

**Option 1**

Ask for a student name.

Display:

- Marks
- Average
- Highest
- Lowest

**Option 2**

Display the class average.

**Option 3**

Pick one random student.

**Option 4**

Exit.

Use:

- Loops
- Dictionaries
- Functions
- `random`
- Exceptions

### Solution

```python
import random

students = {
    "Radhika": [90, 80, 95],
    "Aman": [70, 82, 78],
    "Priya": [99, 95, 97]
}

def average(scores):
    return sum(scores) / len(scores)

while True:
    print("\n1. View Student")
    print("2. View Class Average")
    print("3. Pick Random Student")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Student name: ")

        try:
            marks = students[name]

            print("Marks:", marks)
            print("Average:", average(marks))
            print("Highest:", max(marks))
            print("Lowest:", min(marks))

        except KeyError:
            print("Student not found.")

    elif choice == "2":
        averages = []

        for marks in students.values():
            averages.append(average(marks))

        print("Class Average:", sum(averages) / len(averages))

    elif choice == "3":
        print("Random Student:", random.choice(list(students.keys())))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
```

---

# ⭐⭐⭐ Bonus Challenge

Build the Classroom Manager using **two files**.

## school_utils.py

Move all calculations into this file.

Example:

```python
def average(scores):
    return sum(scores) / len(scores)

def highest(scores):
    return max(scores)

def lowest(scores):
    return min(scores)

def class_average(students):
    averages = []

    for marks in students.values():
        averages.append(average(marks))

    return sum(averages) / len(averages)
```

## main.py

Keep only:

- Menu
- User input
- Printing
- Calls to `school_utils.py`

---

# Concepts Practiced

- Functions
- Dictionaries
- Loops
- Custom modules
- Exception handling
- Random selection
- String methods
- Slicing
- Building menu-driven programs
- Organizing code across multiple files
```
