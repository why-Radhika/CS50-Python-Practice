# Set 2: Conditionals

This set focuses on decision-making in Python using conditional statements.

## Topics Covered

- if
- elif
- else
- Comparison operators
- Modulo operator (%)
- Logical operators
- User input
- String comparison

---

## Question 1 — Positive, Negative, or Zero

### Problem

Ask the user for a number.

**Example**

```text
Enter number: 5
Positive
```

or

```text
Negative
```

or

```text
Zero
```

### Concepts

- if
- elif
- else

---

## Question 2 — Even or Odd

### Problem

Ask the user for an integer.

**Example**

```text
Enter number: 8
Even
```

Use the modulo (`%`) operator.

### Concepts

- if
- else
- modulo operator

---

## Question 3 — Voting Eligibility

### Problem

Ask the user for their age.

Assume the voting age is **18**.

**Example**

```text
Age: 22
Eligible to vote
```

### Concepts

- Comparison operators
- if/else

---

## Question 4 — Password Checker

### Problem

Store the following password:

```python
password = "python123"
```

Ask the user for a password.

Print:

```text
Access Granted
```

or

```text
Access Denied
```

### Concepts

- Strings
- Comparison
- if/else

---

## Question 5 — Largest of Two Numbers

### Problem

Ask the user for two numbers.

Print the larger number.

**Example**

```text
First number: 10
Second number: 25

25 is larger
```

### Concepts

- Comparison operators
- if/elif/else

---

## Question 6 — Grade Calculator

### Problem

Assign grades using the following rules:

| Marks | Grade |
|--------|-------|
| 90+ | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

Ask the user for marks and print the grade.

### Concepts

- Multiple `elif` statements

---

## Question 7 — Leap Year Lite

### Problem

A year is considered a leap year if:

```python
year % 4 == 0
```

Ask the user for a year and print:

```text
Leap Year
```

or

```text
Not Leap Year
```

*(We'll learn the complete leap year rules later.)*

### Concepts

- Modulo operator
- if/else

---

## Question 8 — Movie Ticket Price

### Problem

Use the following pricing rules:

| Age | Ticket Price |
|------|--------------|
| Below 12 | ₹100 |
| 12–59 | ₹200 |
| 60 and above | ₹150 |

Print the ticket price.

### Concepts

- if
- elif
- else

---

## Question 9 — Username Validation

### Problem

Ask the user for a username.

If the username has fewer than **5 characters**, print:

```text
Username too short
```

Otherwise print:

```text
Valid username
```

Use `len()`.

### Concepts

- len()
- if/else

---

## Question 10 — Mini Calculator (Challenge)

### Problem

Ask the user for:

- First number
- Operator (`+`, `-`, `*`, `/`)
- Second number

Example:

```text
First number: 10
Operator: +
Second number: 5

15
```

Use `if`, `elif`, and `else`.

**Bonus:** Handle division by zero.
