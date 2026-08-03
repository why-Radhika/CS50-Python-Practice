"""
Set 9 - Modules, Random, Statistics & Slicing

Note:
For this set, I have not written proper functions and user inputs because
the goal was to understand the lecture concepts and practice them.
"""

# ============================================
# Question 1 — Dice Roller 🎲
# ============================================

import random

roll = random.randint(1, 6)
print("You rolled:", roll)


# ============================================
# Question 2 — Coin Toss 🪙
# ============================================

import random

toss = random.choice(["Heads", "Tails"])
print(toss)


# ============================================
# Question 3 — Lucky Winner 🎉
# ============================================

import random

participants = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul"
]

winner = random.choice(participants)

print("The lucky winner is:", winner)


# ============================================
# Question 4 — Student Statistics 📊
# ============================================

import statistics

marks = [78, 90, 85, 92, 67, 88]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))


# ============================================
# Question 5 — Password Generator (Easy) 🔐
# ============================================

import random

password = random.randint(100000, 999999)

print(password)  # The password may not be very strong.


# ============================================
# Question 6 — Secret Word
# ============================================

word = "Programming"

print(word[:4])      # First 4 letters
print(word[-3:])     # Last 3 letters
print(word[::2])     # Every second character


# ============================================
# Question 7 — Name Formatter
# ============================================

names = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul"
]

print(names[1:4])


# ============================================
# Question 8 — Simple Command-Line Program
# ============================================

import sys

try:
    print("Hello,", sys.argv[1] + "!")
except IndexError:
    print("Usage: python hello.py <name>")


# ============================================
# Question 9 — Create Your First Library 📦
# ============================================

# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


"""
main.py

from calculator import add, subtract, multiply

print(add(2, 4))
print(subtract(4, 2))
print(multiply(2, 4))
"""


# ============================================
# Question 10 — Random Quiz 🎮
# ============================================

import random

questions = [
    "Capital of India?",
    "Largest planet?",
    "Fastest land animal?",
    "Python creator?"
]

quiz = random.choice(questions)

print(quiz)


# ============================================
# ⭐ Bonus Challenge — Create Your First Library
# ============================================

# utilities.py

def is_even(n):
    return n % 2 == 0


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


"""
main.py

from utilities import is_even, square, cube

def main():
    number = int(input("Enter a number: "))

    print(is_even(number))
    print(square(number))
    print(cube(number))

main()
"""