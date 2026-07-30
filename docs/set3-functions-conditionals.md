Set 3 — Lecture 0 + Lecture 1 Combined
Question 1 — Secret Agent

Create a function:

def verify_code(code):

Rules:

If code is "007" → return "Access Granted"
Otherwise → return "Access Denied"

Example:

Enter code: 007
Access Granted

Concepts:

Functions
Parameters
Return values
Strings
Conditionals
Question 2 — Restaurant Discount

Ask for a bill amount.

Rules:

Bill ≥ 1000 → 10% discount
Otherwise → no discount

Output:

Bill: 1200
Final Bill: 1080

Concepts:

Float
if
arithmetic
Question 3 — Username Strength Checker

Create:

def check_username(username):

Rules:

Length < 5 → "Weak"
Length 5–10 → "Good"
Length > 10 → "Strong"

Example:

Enter username: radhika123
Strong

Concepts:

Functions
len()
Conditionals
Question 4 — Number Analyzer

Ask for a number.

Print whether it is:

Positive or Negative
Even or Odd

Example:

Enter number: -8

Negative
Even

Concepts:

Modulo
Multiple conditionals
Question 5 — Smart Greeting

Create:

def greet(name):

Rules:

If name is "Radhika":

Welcome back, Radhika!

Otherwise:

Hello, <name>

Concepts:

Strings
Functions
if
Question 6 — Exam Result Calculator

Ask for:

Marks

Rules:

90+ -> A
80-89 -> B
70-79 -> C
Below 70 -> Fail

Then return:

A
B
C
Fail

from a function.

Example:

grade = calculate_grade(92)
print(grade)

Output:

A

Concepts:

Functions returning values
Conditionals
Question 7 — Mini ATM

Ask for:

Balance
Withdraw amount

Rules:

If withdrawal > balance:

Insufficient Funds

Otherwise:

Remaining Balance: ...

Concepts:

Arithmetic
if/else
Question 8 — Number Comparison Challenge

Create:

def compare(a, b):

Return:

Greater
Smaller
Equal

based on comparison.

Example:

print(compare(10, 5))

Output:

Greater
Question 9 — Leap Year Checker Function

Improve your earlier solution.

Create:

def is_leap(year):

Return:

True

or

False

Then:

if is_leap(year):
    print("Leap Year")
else:
    print("Not Leap Year")

This is good practice for separating logic from output.

Question 10 — FizzBuzz Lite (Challenge)

Ask for a number.

Rules:

Divisible by 3 → print "Fizz"
Divisible by 5 → print "Buzz"
Divisible by both → print "FizzBuzz"
Otherwise print the number

Examples:

15 → FizzBuzz
9 → Fizz
10 → Buzz
7 → 7

This is a famous interview-style beginner problem.

Hint

Be careful with the order of conditions.

Bonus Challenge (Most Interesting)

Create a function:

def login(username, password):

Rules:

username = "admin"
password = "python123"

Return:

Login Successful

only if both are correct.

Otherwise return:

Invalid Credentials

Use and.
