# Set 8: Exception Handling

This set introduces exception handling in Python. The goal is to write programs that continue running even when users enter invalid input.

## Topics Covered

- try
- except
- ValueError
- while loops
- Input validation
- Functions
- Defensive programming

---

# Question 1 — Safe Integer Input

## Problem

Ask the user for an integer.

If the user enters invalid input such as:

```
abc
```

Print:

```
Invalid input. Please enter an integer.
```

Otherwise print:

```
You entered 25
```

## Concepts

- try
- except
- ValueError

---

# Question 2 — Keep Asking

## Problem

Improve Question 1.

Keep asking until the user enters a valid integer.

### Example

```
Enter age: abc
Invalid input

Enter age: hello
Invalid input

Enter age: 22
Age accepted.
```

## Concepts

- while loop
- try/except

---

# Question 3 — Positive Integer

## Problem

Ask for an integer.

Rules:

- Must be an integer.
- Must be greater than 0.

### Example

```
Enter number: -5
Must be positive.

Enter number: abc
Invalid input.

Enter number: 10
Accepted.
```

## Concepts

- Input validation
- Loops
- Exceptions

---

# Question 4 — Safe Division

## Problem

Ask for two integers.

Print:

```
Result = ...
```

Handle:

- Invalid numbers
- Division by zero

### Example

```
First number: 10
Second number: 0

Cannot divide by zero.
```

## Concepts

- try/except
- ZeroDivisionError

---

# Question 5 — Create Your Own Function

## Problem

Create:

```python
get_integer()
```

The function should:

- Keep asking
- Return a valid integer

Then use it:

```python
num1 = get_integer()
num2 = get_integer()

print(num1 + num2)
```

## Concepts

- Functions
- Return values
- Exception handling

---

# Question 6 — Guess the Number (Exception Edition)

## Problem

Secret number:

```
7
```

If the user enters:

```
abc
```

Don't crash.

Instead print:

```
Please enter a valid number.
```

Continue until the correct number is guessed.

## Concepts

- while loop
- Exception handling

---

# Question 7 — Menu Program

## Problem

Display the menu:

```
1. Add
2. Subtract
3. Exit
```

If the user enters invalid input such as:

```
hello
```

Don't crash.

Keep displaying the menu.

## Concepts

- while loop
- Exception handling

---

# Question 8 — BMI Calculator (Improved)

## Problem

Reuse your BMI Calculator.

Handle:

- Text instead of weight
- Text instead of height
- Zero height
- Negative values

The program should never crash.

## Concepts

- Input validation
- Exception handling

---

# Question 9 — Student Marks

## Problem

Ask for marks.

Rules:

- Integer only
- Between 0 and 100

Keep asking until the input is valid.

## Concepts

- Validation
- Loops
- Exceptions

---

# Question 10 — ATM (Exception Edition)

## Problem

Reuse your ATM project.

Handle invalid input such as:

```
Withdraw amount:
abc
```

or

```
Menu option:
hello
```

The ATM should continue running without crashing.

## Concepts

- Exception handling
- Menu-driven programs
- Validation

---

# ⭐ Bonus Challenge

## Problem

Create:

```python
def get_int(prompt):
```

Example:

```python
age = get_int("Age: ")
marks = get_int("Marks: ")
salary = get_int("Salary: ")
```

The function should:

- Accept any prompt
- Never crash
- Always return a valid integer

This is a reusable helper function that can be used in many future programs.

## Restrictions

- Do **not** use `except:` by itself.
- Catch specific exceptions such as `ValueError`.
- Keep input handling separate from calculation logic whenever possible.
